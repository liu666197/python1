import requests,csv
from lxml import etree

#下载图片
def download(url):
    # url = 'https://www.baidu.com/img/flexible/logo/pc/result.png'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    response = requests.get(url, headers=headers)
    # 文件的返回数据: 二进制数据
    # print(response.content)
    # 图片的名字
    # 获取最后一个/出现的位置
    index = url.rfind('/')
    if index != -1:
        name = 'images' + url[index:]
    #  images/xx.png
    # 下载: 二进制数据保存到本地
    with open(name, 'wb') as file:
        file.write(response.content)

# 爬取一页数据的函数
def getData(page):
    global count
    url = 'https://www.zcool.com.cn/'
    dic = {
        'p': page
    }
    # 2.请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    # 发送请求
    response = requests.get(url, headers=headers, params=dic)
    # 源代码
    content = response.text
    # with open('1.html','w',encoding='utf-8') as file:
    #     file.write(content)

    # 把代码字符串转换成标签对象
    html = etree.HTML(content)
    # 先拿到每条数据的标签
    divElements = html.xpath('//div[@class="card-box"]')
    # count = 0
    # 拿到每条数据
    for div in divElements:
        # 从当前标签元素获取数据
        url = div.xpath('./div[@class="card-img"]//img/@src')[0]
        # 下载图片
        download(url)
        title = div.xpath('./div[@class="card-img"]//img/@title')[0]
        type = div.xpath('.//p[@class="card-info-type"]/text()')[0]
        dataCount = div.xpath('.//p/span/text()')
        if len(dataCount) > 0:
            watch, pinglun, dianzan = dataCount
        else:
            watch, pinglun, dianzan = '无', '无', '无'
        author = div.xpath('.//div[@class="card-item"]//a/@title')[0]
        # 每条数据的字典
        dic = {
            'url地址': url,
            '作品名': title,
            '作品类型': type,
            '人气数': watch,
            '评论数': pinglun,
            '点赞数': dianzan,
            '作者': author
        }
        # 次数+1
        count += 1
        print(count, '++++')
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

count = 0
for page in range(1,11):
    print('第{}页开始'.format(page))
    # 爬取一页的代码
    getData(page)
    print('第{}页结束'.format(page))