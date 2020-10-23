import urllib.request,urllib.parse
# 1.url地址
url = 'https://www.zhisheji.com/new_index_tj'

# 2.请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
# post的参数
dic = {
    'page': 1
}
# 转化为Unicode编码-->二进制数据
result = urllib.parse.urlencode(dic).encode()

# 3.构建网络请求 (data: post请求的参数)
request = urllib.request.Request(url, headers=headers,data=result)

# 4.响应对象
response = urllib.request.urlopen(request)

# 5.数据 (源代码)
content = response.read().decode()

# 6.保存一页到本地,看展示效果
with open('1.html','w',encoding='utf-8') as file:
    file.write(content)