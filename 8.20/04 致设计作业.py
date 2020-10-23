import re,csv,urllib.request

# 1.url (网址)
# url = 'https://www.zcool.com.cn/'
url = 'https://www.zhisheji.com/'
# 2.请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
# 3.构建网络请求
request = urllib.request.Request(url,headers = headers)

# 4.响应对象
response = urllib.request.urlopen(request)

# 5.数据 (源代码)
content = response.read().decode()
# 6.保存一页到本地,看展示效果
# with open('1.html','w',encoding='utf-8') as file:
#     file.write(content)
# 7. 获取到每条数据的整体源代码
pattern = r'<li id=".+?">(.+?)</li>'
result = re.findall(pattern,content,re.S)
count = 0
# 所有的数据
allResult = []
# 8.遍历每条数据的源代码,再该源代码的基础之上匹配数据
for dataStr in result:
    count += 1
    print(count,'+++++')
    # url和标题
    pattern = r'<img class="previews" mysrc="(.+?)" src="" alt="(.+?)" width="290" height="180" alt="fads">'
    url,title = re.findall(pattern,dataStr,re.S)[0]
    # 类型
    pattern = r'<div class="desc">(.+?)</div>'
    typeResult = re.findall(pattern,dataStr,re.S)[0]
    # 观看人数
    # pattern = r'<em><span class="icon-view"></span>(.+?)</em>'
    # 直接取三个值
    pattern = r'<em><span class="icon-view"></span>(.+?)</em>\s+<em><span class="icon-praise"></span>(.+?)</em>\s+<em><span class="icon-comment"></span>(.+?)</em>'
    watchResult,dianzanResult,pinglunResult = re.findall(pattern,dataStr,re.S)[0]
    # 头像和作者
    pattern = r'<div class="sjs-name">\s+<a target="_blank" href=".+?" title="(.+?)">\s+<img class="previews" mysrc="(.+?)" src="" height="120" width="120"'
    author,icon = re.findall(pattern, dataStr, re.S)[0]
    # 构建每条数据
    dic = {
        'url地址': url,
        '作品名': title,
        '作品类型': typeResult,
        '观看人数': watchResult,
        '点赞数': dianzanResult,
        '评论数': pinglunResult,
        '作者': author,
        '头像': icon
    }
    allResult.append(dic)
# 表头
header = ['url地址', '作品名', '作品类型', '观看人数', '点赞数', '评论数', '作者','头像']

# 存入csv
with open('致设计.csv', 'w', encoding='utf-8-sig', newline='') as file:
    # 写入者
    csv_file = csv.DictWriter(file, header)
    # 写入表头
    csv_file.writeheader()
    # 写入所有数据
    csv_file.writerows(allResult)