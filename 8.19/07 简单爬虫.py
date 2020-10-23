import urllib.request,re
# https://www.zcool.com.cn/?p=1#tab_anchor
# https://www.zcool.com.cn/?p=2#tab_anchor
# https://www.zcool.com.cn/?p=3#tab_anchor
# 1.准备网址
url = 'https://www.zcool.com.cn/'

# 2.请求头 字典 (模拟浏览器)
a = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
# 3.构建网络请求 (headers: 请求头)
request = urllib.request.Request(url,headers=a)

# 4.发送网络请求 (返回值就是服务器响应对象)
response = urllib.request.urlopen(request)
# 5.response.read(): 服务器响应的源代码,是一个二进制数据

# 6.对二进制数据进行解码操作 (源代码)
content = response.read().decode()

# 7.查看是否给我们返回的是对应的网页(把源代码保存到本地,在浏览器打开看看)
with open('1.html','w',encoding='utf-8') as file:
    file.write(content)

# 8.解析数据
# pattern = r'class="mnav c-font-normal c-color-t">(.+?)</a>'
# result = re.findall(pattern,content,re.S)
# print(result)

# print(content)