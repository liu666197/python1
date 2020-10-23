import requests
url = 'http://news.baidu.com/widget?id=civilnews'
# 2.请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
response = requests.get(url,headers=headers)
with open('1.html','w',encoding='utf-8') as file:
    file.write(response.text)
