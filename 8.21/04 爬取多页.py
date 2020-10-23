import requests,csv
from lxml import etree

def getData(page):
    global count
    url = 'https://www.zhisheji.com/new_index_tj'
    # 2.请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    # post请求
    response = requests.post(url, headers=headers, data={'page': page})
    # with open('1.html','w',encoding='utf-8') as file:
    #     file.write(response.text)
    # count = 0
    # 源代码
    content = response.text
    # 转化为html元素
    html = etree.HTML(content)
    # 每条数据的标签
    liElements = html.xpath('//ul[@class="list"]/li')
    # 从每个li标签取数据
    for li in liElements:
        url = li.xpath('.//span/img/@mysrc')[0]
        title = li.xpath('.//span/img/@alt')[0]
        watch, pinglun, dianzan = li.xpath('.//em/text()')
        type = li.xpath('./div[@class="desc"]/text()')[0]
        icon = li.xpath('.//div[@class="sjs-name"]//img/@mysrc')[0]
        author = li.xpath('.//div[@class="sjs-name"]//a/@title')[0]
        # 构建每条数据
        dic = {
            'url地址': url,
            '作品名': title,
            '作品类型': type,
            '观看人数': watch,
            '点赞数': pinglun,
            '评论数': dianzan,
            '作者': author,
            '头像': icon
        }
        count += 1
        # 表头
        header = ['url地址', '作品名', '作品类型', '观看人数', '点赞数', '评论数', '作者', '头像']

        # 存入csv
        with open('致设计.csv', 'a', encoding='utf-8-sig', newline='') as file:
            # 写入者
            csv_file = csv.DictWriter(file, header)
            if count == 1:
                # 写入表头
                csv_file.writeheader()
            # 写入所有数据
            csv_file.writerow(dic)

# 爬多页
count = 0
for page in range(1,11):
    print('第{}页开始'.format(page))
    # 爬取一页的代码
    getData(page)
    print('第{}页结束'.format(page))