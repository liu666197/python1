import requests
from lxml import etree

# 文件下载
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
        name = '简历' + url[index:]
    #  images/xx.png
    # 下载: 二进制数据保存到本地
    with open(name, 'wb') as file:
        file.write(response.content)

url = 'http://sc.chinaz.com/jianli/free.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
response = requests.get(url,headers = headers)
# 设置响应数据的编码格式
response.encoding = 'utf-8'

# 拿到一级页面要跳转到二级页面的网址
html = etree.HTML(response.text)
# 找到每条数据
allData = html.xpath('//div[@class="box col3 ws_block"]')
for strData in allData:
    # 一级页面要跳转到二级页面的网址
    href,title = strData.xpath('./a/@href|./a/img/@alt')
    print(href,title)
    # 发送二级页面的请求
    erjiResponse = requests.get(href,headers = headers)
    erjiResponse.encoding = 'utf-8'
    erjiData = etree.HTML(erjiResponse.text)
    # 文件地址
    erjiResult = erjiData.xpath('//div[@class="clearfix mt20 downlist"]//li[1]/a/@href')[0]
    # 文件名: 简历名.rar
    # 下载
    download(erjiResult)
    # with open('1.html','w',encoding='utf-8') as file:
    #     file.write(erjiResponse.text)