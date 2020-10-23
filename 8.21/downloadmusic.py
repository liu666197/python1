import requests,os


# 文件下载
def download(url,name):
    # url = 'https://www.baidu.com/img/flexible/logo/pc/result.png'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    response = requests.get(url, headers=headers)
    # 文件的返回数据: 二进制数据
    # print(response.content)
    # 图片的名字
    # 创建文件夹
    dirName = 'music'
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    name = dirName + '/' + name + '.mp3'
    #  images/xx.png
    # 下载: 二进制数据保存到本地
    with open(name, 'wb') as file:
        file.write(response.content)

# 用户输入
userInput = input('请输入要下载的歌手名: ')

# 获得每首歌的信息
singerUrl = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?httpsStatus=1&reqId=3b70b8a0-e385-11ea-9da7-4b2b837551a3'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1597997140; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1597997140; _ga=GA1.2.808148247.1597997140; _gid=GA1.2.1873191306.1597997140; _gat=1; kw_token=6ZHFHUTWA3D',
    'csrf': '6ZHFHUTWA3D',
    # 当前的网页从哪个网页中跳转过来的
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%BC%A0%E6%9D%B0'
}
dic = {
    'key': userInput,
    # 每页个数
    'rn': 30,
    'pn': 1
}
response = requests.get(singerUrl,headers = headers,params=dic)
# 先使用text进行测试
# print(response.text)
allData = response.json()['data']['list']
count = 0
# 拿到每首歌曲信息
for musicData in allData:
    count += 1
    print(count,'+++')
    # 每首歌的序号
    rid = musicData['rid']
    # 每首歌的名字
    musicName = musicData['name']
    print(musicName)
    # 根据序号发送歌曲的网络请求
    musicUrl = 'http://www.kuwo.cn/url?format=mp3&rid=%s&response=url&type=convert_url3&br=128kmp3&from=web&t=1597997853339&httpsStatus=1&reqId=c381adc1-e386-11ea-9da7-4b2b837551a3'%(rid)
    # 新的请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    # 每首歌信息的响应
    musicReponse = requests.get(musicUrl,headers = headers)
    # mp3地址
    musicFileUrl = musicReponse.json()['url']
    # 下载
    download(musicFileUrl,musicName)
    print('%s下载成功'%(musicName))
    # print(rid)
# print(allData,len(allData))