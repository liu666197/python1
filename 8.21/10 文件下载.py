import requests

url = 'https://www.baidu.com/img/flexible/logo/pc/result.png'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
response = requests.get(url,headers = headers)
# 文件的返回数据: 二进制数据
# print(response.content)
# 图片的名字
# 获取最后一个/出现的位置
index = url.rfind('/')
if index != -1:
    name = 'images' + url[index:]
#  images/xx.png
# 下载: 二进制数据保存到本地
with open(name,'wb') as file:
    file.write(response.content)
