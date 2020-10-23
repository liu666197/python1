import requests,os


# 文件下载
def download(url,name):
    # url = 'https://www.baidu.com/img/flexible/logo/pc/result.png'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    response = requests.get(url, headers=headers)
    #  images/xx.png
    # 下载: 二进制数据保存到本地
    with open(name, 'wb') as file:
        file.write(response.content)

url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}

response = requests.get(url,headers=headers)
allData = response.json()['hero']
# 总体文件夹
dirs = 'images'
if not os.path.exists(dirs):
    os.mkdir(dirs)
count = 0
# 没一个英雄
for hero in allData:
    count += 1
    print(count,hero['name'])
    # 文件夹路径
    heroName = dirs + '/' + hero['name']
    # id
    heroId = hero['heroId']
    # 每个英雄的文件夹
    if not os.path.exists(heroName):
        os.mkdir(heroName)
    # 发送皮肤的请求
    skinUrl = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'.format(heroId)
    skinResponse = requests.get(skinUrl,headers=headers)
    skins = skinResponse.json()['skins']
    # 每个皮肤
    for skin in skins:
        imgUrl = skin['mainImg'] or skin['chromaImg']
        # 取后缀
        index = imgUrl.rfind('.')
        # 皮肤名字
        skinName = heroName + skin['name'].replace('/','') + imgUrl[index:]
        # print(skinName)
        # 下载图片
        download(imgUrl,skinName)