import re,csv
with open('zhanku.html','r',encoding='utf-8') as file:
    # 所有源代码
    content = file.read()

# 1.获取到每条数据的整体源代码
pattern = r'<div class="card-box">(.+?)</div>\s+</div>'
# result: 每条数据的整体源代码
result = re.findall(pattern,content,re.S)
count = 0
# 所有的数据
allResult = []
# 2.遍历每条数据的源代码(拿到每条数据的源代码) dataStr
for dataStr in result:
    count += 1
    print(count,'++++')
    # 把规则与每条数据的源代码进行匹配
    # url地址和作品名字
    pattern = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
    urlAndTitleResult = re.findall(pattern,dataStr,re.S)[0]
    # url地址
    url = urlAndTitleResult[1] or urlAndTitleResult[4]
    # 作品名
    title = urlAndTitleResult[2] or urlAndTitleResult[5]
    # 作品类型
    pattern = r'<p class="card-info-type" title="(.+?)">'
    typeResult = re.findall(pattern,dataStr,re.S)[0]
    # 人气数 (38)
    pattern = r'<span class="statistics-view" title="共(.+?)人气">'
    fansResult = re.findall(pattern,dataStr,re.S)
    # 说明有数据
    if len(fansResult) > 0:
        fansResult = fansResult[0]
    else:
        fansResult = '无'
    # 评论数
    pattern = r'<span class="statistics-comment" title="共(.+?)评论">'
    pinglunResult = re.findall(pattern, dataStr, re.S)
    if len(pinglunResult) > 0:
        pinglunResult = pinglunResult[0]
    else:
        pinglunResult = '无'
    # 点赞数
    pattern = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
    dianzanResult = re.findall(pattern, dataStr, re.S)
    if len(dianzanResult) > 0:
        dianzanResult = dianzanResult[0]
    else:
        dianzanResult = '无'
    # 作者
    pattern = r'(<span class="user-avatar showMemberCard">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(class="card-item">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="content_ad_publisher">)'
    authorResult = re.findall(pattern,dataStr,re.S)[0]
    authorResult = authorResult[1] or authorResult[3]
    # 每条数据的字典
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

# 表头
header = ['url地址','作品名','作品类型','人气数','评论数','点赞数','作者']

# 存入csv
with open('站酷1.csv','w',encoding='utf-8-sig',newline='') as file:
    # 写入者
    csv_file = csv.DictWriter(file,header)
    # 写入表头
    csv_file.writeheader()
    # 写入所有数据
    csv_file.writerows(allResult)

print('hello world')