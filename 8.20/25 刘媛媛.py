# 1.站酷解析(10页数据,requests结合xpath)  get
import re,csv,requests

# 获取数据
count=0
# 要爬取站酷10页的数据
for page in range(1,11):
    # print('从第{}页开始'.format(page))
    # 1.url (网址)
    url = 'https://www.zcool.com.cn/?p=%s#tab_anchor' % (page)
    # 2.请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    # 3.get请求(直接有返回对象)
    response = requests.get(url, headers=headers)
    # 获得文本数据
    content = response.text
    # 4.利用xpath语法解析数据
    html = etree.HTML(content)
    result = html.xpath('//div[@class="card-box"]')
    print(len(result))
    # 遍历数据
    for i in result:
        count +=1
        url = i.xpath('.//div[@class="card-img"]/a/img/@src')[0]
    # 标题
    title = i.xpath('.//div[@class="card-img"]/a/img/@title')[0]
    #类型
    type = i.xpath('.//p[@class="card-info-type"]/@title')[0]
    # 人气-38
    renqi = i.xpath('.//span[@class="statistics-view"]/text()')
    if len(renqi) == 0:
        renqi = '无'
    else:
        renqi = renqi[0]
     # 评论38条
    pinglun = i.xpath('.//span[@class="statistics-comment"]/text()')
    if len(pinglun) == 0:
        pinglun = '无'
    else:
        pinglun = pinglun[0]
     # 赞38条
    zan = i.xpath('.//span[@class="statistics-tuijian"]/text()')
    if len(zan) == 0:
        zan= '无'
    else:
        zan = zan[0]
    # 作者
    author = i.xpath( './/div[@class="card-item"]/span/a/@title')
    if len(author) == 0:
        author = html.xpath('//div[@class="card-item"]/a/@title')
        author =author[0]
    dic = {
            'url地址': url,
            '作品名': title,
            '作品类型': type,
            '人气数': renqi,
            '评论数': pinglun,
            '点赞数': zan,
            '作者': author
                }
    # 第三步:写入csv
    header = ['url地址', '作品名', '作品类型', '人气数', '评论数', '点赞数', '作者']
    # 存入csv
    with open('站酷.csv', 'a', encoding='utf-8-sig', newline='') as file:
    # 写入者
         csv_file = csv.DictWriter(file, header)
    #写入表头
         if count == 1:
          csv_file.writeheader()
    # 写入所有数
         csv_file.writerow(dic)
    print('{}页结束'.format(page))
# 2.致设计解析(10页数据,requests结合xpath) post
# 老师,我只完成了一道作业题,还有两分钟就凌晨了,我实在写不动了,我先睡了,周末把作业补齐zzzzzzz