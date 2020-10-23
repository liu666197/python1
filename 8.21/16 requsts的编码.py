import requests

url = 'https://lol.qq.com/data/info-heros.shtml'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
reponse = requests.get(url,headers=headers)
# 设置响应数据的编码格式(和源代码的编码一样)
# <meta charset="gb2312"/>
reponse.encoding = 'gb2312'
print(reponse.text)