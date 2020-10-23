import requests
from base import download
# rn: 每页的数据条数
# pn: rn * page
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E4%BD%A9%E5%A5%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E4%BD%A9%E5%A5%87&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=55&gsm=1e&1597988871073='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
response = requests.get(url,headers = headers)
# 服务器返回的如果是json数据,使用json()
content = response.json()
# 所有的图片数据
count = 0
# 所有的数据(最后一项没有)
allData = content['data'][:len(content['data']) - 1]
for img in allData:
    count += 1
    print(count,'++++')
    # 所有图片的url地址
    # print(img['hoverURL'])
    download(img['hoverURL'])