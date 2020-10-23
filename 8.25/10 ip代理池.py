import requests,random
# ip地址的api
api_url = 'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=1&fa=0&fetch_key=&groupid=0&qty=10&time=1&pro=%E5%8C%97%E4%BA%AC%E7%9B%B4%E8%BE%96%E5%B8%82&city=%E5%8C%97%E4%BA%AC%E5%B8%82&port=1&format=html&ss=5&css=&dt=1&specialTxt=3&specialJson=&usertype=15'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}
response = requests.get(api_url,headers = headers)
# 分割为列表
ipdata = response.text.split('<br>')
ipList = []
for ip in ipdata:
    dic = {'https': ip}
    ipList.append(dic)
# 发送请求的时候从ip代理池里面随机取一个ip来发送请求
url = 'https://www.kuaidaili.com/free/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}
while True:
    try:
        # 一个ip地址不行,程序崩溃
        ip = random.choice(ipList)
        response = requests.get(url, headers=headers, proxies=ip)
        # 循环得终止
        break
    except:
        print(ip,'不行')
with open('快代理.html','w',encoding='utf-8') as file:
    file.write(response.text)