import re,csv,urllib.request,random

# 所有的数据
allResult = []

# user-agent列表
userAgentList = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)'
]
# 爬取的数据条数
count = 0
for page in range(1,11):
    print('第{}页开始'.format(page))
    # 1.url (网址)
    # url = 'https://www.zcool.com.cn/'
    url = 'https://www.zcool.com.cn/?p=%s#tab_anchor'%(page)
    # 2.请求头
    headers = {
        'User-Agent': random.choice(userAgentList)
    }
    # 3.构建网络请求
    request = urllib.request.Request(url, headers=headers)

    # 4.响应对象
    response = urllib.request.urlopen(request)

    # 5.数据 (源代码)
    content = response.read().decode()

    # 6.保存一页到本地,看展示效果
    # with open('1.html','w',encoding='utf-8') as file:
    #     file.write(content)

    # 1.获取到每条数据的整体源代码
    pattern = r'<div class="card-box">(.+?)</div>\s+</div>'
    # result: 每条数据的整体源代码
    result = re.findall(pattern, content, re.S)

    # 2.遍历每条数据的源代码(拿到每条数据的源代码) dataStr
    for dataStr in result:
        # 把规则与每条数据的源代码进行匹配
        # url地址和作品名字
        pattern = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
        urlAndTitleResult = re.findall(pattern, dataStr, re.S)[0]
        # url地址
        url = urlAndTitleResult[1] or urlAndTitleResult[4]
        # 作品名
        title = urlAndTitleResult[2] or urlAndTitleResult[5]
        # 作品类型
        pattern = r'<p class="card-info-type" title="(.+?)">'
        typeResult = re.findall(pattern, dataStr, re.S)[0]
        # 人气数 (38)
        pattern = r'<span class="statistics-view" title="共(.+?)人气">'
        fansResult = re.findall(pattern, dataStr, re.S)
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
        # pattern = r'(<span class="user-avatar showMemberCard">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(class="card-item">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="content_ad_publisher">)|(<span class="user-avatar">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)'
        pattern = r'(<span class="user-avatar.*?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(class="card-item">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="content_ad_publisher">)'
        authorResult = re.findall(pattern, dataStr, re.S)[0]
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
        # 次数+1
        count += 1
        print(count,'++++')
        # 表头
        header = ['url地址', '作品名', '作品类型', '人气数', '评论数', '点赞数', '作者']
        # 存入csv (爬一条存一条)
        with open('站酷.csv', 'a', encoding='utf-8-sig', newline='') as file:
            # 写入者
            csv_file = csv.DictWriter(file, header)
            if count == 1:
                # 写入表头(第一条数据的时候写入表头)
                csv_file.writeheader()
            # 写入所有数据
            csv_file.writerow(dic)
    print('第{}页结束'.format(page))

# 当所有的数据爬取完毕以后,再进行数据持久化


