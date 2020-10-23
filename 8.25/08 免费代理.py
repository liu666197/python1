import requests
url = 'https://www.kuaidaili.com/free/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}
response = requests.get(url,headers = headers,proxies = {'https': '123.207.217.179:1080'})
with open('快代理.html','w',encoding='utf-8') as file:
    file.write(response.text)