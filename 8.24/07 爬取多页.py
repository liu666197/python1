import requests,csv,pymysql,json
from lxml import etree

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
        # 加入到列表里面
        allData.append(dic)
        # 存入到json数据
        data = {'data': allData}
        with open('站酷.json','w',encoding='utf-8') as file:
            # 直接存入json
            json.dump(data,file,ensure_ascii=False,indent=4)
        # 次数+1
        count += 1
        print(count, '++++')
        # 存入数据库 (将单引号替换为空)
        sql = "INSERT INTO zcool (url,title,type,fans,pinglun,dianzan,author) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (
        url, title.replace("'","\\'"),type,watch,pinglun,dianzan,author)
        print(sql)
        # 执行sql
        cursor.execute(sql)
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
# 连接数据库
db = pymysql.connect('localhost','root','','python')
# 生成游标对象
cursor = db.cursor()
# 所有的数据
allData = []
for page in range(6,11):
    print('第{}页开始'.format(page))
    # 爬取一页的代码
    getData(page)
    print('第{}页结束'.format(page))

#提交操作
db.commit()
# 关闭数据库
db.close()