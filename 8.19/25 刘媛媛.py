# 站酷: https://www.zcool.com.cn/
# 把该网站的数据保存400条下来;格式和周五要求的格式一样
import urllib.request
import re
import csv
contentAll = ''
for i in range(1,11):
    # 要爬取的内容网址
    url = 'https://www.zcool.com.cn/?p=%s#tab_anchor' % (i)
   # 模拟浏览器,写请求头,用字典形式表示
    a = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
  # 构建网络请求(headers: 请求头)
    request = urllib.request.Request(url, headers=a)
    # 发送网络请求,其返回值就是服务器响应对象
    response = urllib.request.urlopen(request)
    # response.read(): 服务器响应的源代码,是一个二进制数据,对二进制数据进行解码操作(将其转为字符串) (源代码)
    content = response.read().decode()
    # 查看是否给我们返回的是对应的网页(把源代码保存到本地,在浏览器打开看看)
    # with open('致设计1.html','w',encoding='utf-8') as file:
    #     file.write(content)
    contentAll += content
    # print(contentAll)
    # with open('站酷十页.html','w',encoding='utf-8') as file:
    #     file.write(contentAll)

    # 获取到每条数据的整体源代码(<div class="card-box card-box_gogoup">)
pattern = r'<div class="card-box">(.+?)</div>\s+</div>'
# result: 每条数据的整体源代码
result = re.findall(pattern, contentAll, re.S)
count = 0
# 所有的数据
allResult = []
# 遍历每条数据的源代码(拿到每条数据的源代码) dataStr
for dataStr in result:
    count += 1
    # print(dataStr)
    #   把规则与每条数据的源代码进行匹配
    #   url地址和作品名字
    pattern = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
    urlAndTitleResult = re.findall(pattern, dataStr, re.S)[0]
    # url地址
    url = urlAndTitleResult[1] or urlAndTitleResult[4]
    # 作品名
    title = urlAndTitleResult[2] or urlAndTitleResult[5]
    #     # # 作品类型
    pattern = r'<p class="card-info-type" title="(.+?)">'
    typeResult = re.findall(pattern, dataStr, re.S)[0]
    #     # 人气数 (38)
    pattern = r'<span class="statistics-view" title="共(.+?)人气">'
    fansResult = re.findall(pattern, dataStr, re.S)
    #     # 说明有数据
    if len(fansResult) > 0:
        fansResult = fansResult[0]
    else:
        fansResult = '无'
    #     # 评论数
    pattern = r'<span class="statistics-comment" title="共(.+?)评论">'
    pinglunResult = re.findall(pattern, dataStr, re.S)
    if len(pinglunResult) > 0:
        pinglunResult = pinglunResult[0]
    else:
        pinglunResult = '无'
    #     # 点赞数
    pattern = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
    dianzanResult = re.findall(pattern, dataStr, re.S)
    if len(dianzanResult) > 0:
        dianzanResult = dianzanResult[0]
    else:
        dianzanResult = '无'
    #     # 作者
    pattern = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
    authorResult = re.findall(pattern, dataStr, re.S)[0]
    # print(authorResult)
    authorResult = authorResult[1] or authorResult[3]
    # print(authorResult)
    #     # 每条数据的字典
    dic = {
        'url地址': url,
        '作品名': title,
        '作品类型': typeResult,
        '人气数': fansResult,
        '评论数': pinglunResult,
        '点赞数': dianzanResult,
        '作者': authorResult
    }
    allResult.append(dic)
# print(count)
# # 表头
header = ['url地址', '作品名', '作品类型', '人气数', '评论数', '点赞数', '作者']

# 存入csv
with open('站酷十页.csv', 'w', encoding='utf-8-sig', newline='') as file:
    # 写入者
    csv_file = csv.DictWriter(file, header)
    # 写入表头
    csv_file.writeheader()
    # 写入所有数
    csv_file.writerows(allResult)






# # 2.致设计: https://www.zhisheji.com/
# # 保存该网页的第一页的数据,存入到csv
# import urllib.request
# import re
# import csv
# # 1.准备网址
# url = 'https://www.zhisheji.com/'
# # 2.请求头 字典 (模拟浏览器)
# a = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
# }
# # 3.构建网络请求 (headers: 请求头)
# request = urllib.request.Request(url,headers=a)
# # 4.发送网络请求 (返回值就是服务器响应对象)
# response = urllib.request.urlopen(request)
# # 5.对二进制数据进行解码操作 (源代码)
# content = response.read().decode()
#  # 6.查看是否给我们返回的是对应的网页(把源代码保存到本地,在浏览器打开看看)
# with open('zhisheji.html','w',encoding='utf-8') as file:
#     file.write(content)
#
# # 读网页源代码
# with open('zhisheji.html', 'r', encoding='utf-8') as file:
#
#         content = file.read()
# # 整个网页的源代码
# pattern = r'<li id=".+?">(.+?)</li>'
# result = re.findall(pattern,content,re.S)
# # 取数据 遍历代码
# allData = []
# count = 0
# for dataStr in result:
#     # 取url和title
#     pattern = r'<a target="_blank" href=".+?" title="(.+?)">\s+<span class="img-box"><img class="previews" mysrc="(.+?)" src="" alt=".+?" width="290" height="180"'
#     urlAndTitleResult = re.findall(pattern,dataStr,re.S)[0]
#     # print(urlAndTitleResult)
#     url = urlAndTitleResult[1]
#     title = urlAndTitleResult[0]
#     # print(url,title)
#     # 取type
#     pattern = r'<div class="desc">(.+?)</div>'
#     type = re.findall(pattern,dataStr,re.S)[0]
#     # print(type)
#     # 取人气 评论 赞
#     # 人气
#     pattern = r'<em><span class="icon-view"></span>(.+?)</em>'
#     renqi = re.findall(pattern, dataStr, re.S)[0]
#     # print(renqi)
#     # 赞
#     pattern = r'<em><span class="icon-praise"></span>(.+?)</em>'
#     zan = re.findall(pattern, dataStr, re.S)[0]
#     # 评论
#     pattern = r'<em><span class="icon-comment"></span>(.+?)</em>'
#     pinglun = re.findall(pattern, dataStr, re.S)[0]
#     # 取作者及作者图片地址
#     pattern = r'title=".+?">\s+<img class="previews" mysrc="(.+?) src="" height="120" width="120" alt="(.+?)"'
#     authorResult = re.findall(pattern,dataStr,re.S)[0]
#     # print(authorResult)
#     author = authorResult[1]
#     authorUrl = authorResult[0]
#     # print(url,title,type,renqi,zan,pinglun,author,authorUrl)
#     count += 1
#     dic = {
#         'url地址': url,
#         '作品名': title,
#         '作品类型': type,
#         '人气数': renqi,
#         '评论数': pinglun,
#         '点赞数': zan,
#         '作者': author,
#         '作者头像url地址': authorUrl
#     }
#     allData.append(dic)
# # print(allData)
# # # print(count)
#
#
# # 表头
# header = ['url地址', '作品名', '作品类型', '人气数', '评论数', '点赞数', '作者','作者头像url地址']
# # 存入csv
# with open('致设计.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     # 写入者
#     csv_file = csv.DictWriter(file, header)
#     # 写入表头
#     csv_file.writeheader()
#     # 写入所有数据
#     csv_file.writerows(allData)