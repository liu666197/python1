import requests

url = 'https://www.zhisheji.com/new_index_tj'
# 2.请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
}
# post参数是字典类型
dic = {
    'page': 1
}
# post请求(直接有返回对象)
response = requests.post(url,headers = headers,data=dic)
# 源代码(bytes类型)
# print(response.content)
# 源代码(字符串类型)
# print(response.text)
with open('3.html','w',encoding='utf-8') as file:
    file.write(response.text)