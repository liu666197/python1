import urllib.request,urllib.parse
userInput = input('请输入要搜索的内容: ')
# 将参数的中文转化为Unicode编码方式
dic = {
    'keyword': userInput,
}
# 转化
result = urllib.parse.urlencode(dic)
# wd=%E5%93%88%E5%93%88%E5%93%88
print(result)
url = 'https://search.jd.com/Search?'+result
print(url)
# 2.请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Cookie': 'BIDUPSID=50759B98EE1CC67940BDD904C1EEE7A0; PSTM=1597025934; BAIDUID=50759B98EE1CC67943C44CCF0D1A9339:FG=1; BD_UPN=12314353; MCITY=-131%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ispeed_lsm=2; delPer=0; BD_CK_SAM=1; PSINO=1; BD_HOME=1; H_PS_PSSID=1431_32572_32350_32045_32116_31321_32498; H_PS_645EC=925doEoUyzm3T9H3qlGOLsl%2FTGrIzC7CmS%2BA%2FBJgoHKAEtWDT7o6vm1H1WM; COOKIE_SESSION=41_4_7_9_47_14_0_0_6_8_4_1_0_0_0_0_1597799414_1597802797_1597893958%7C9%230_1_1597802799%7C1'
}
# 3.构建网络请求
request = urllib.request.Request(url, headers=headers)

# 4.响应对象
response = urllib.request.urlopen(request)

# 5.数据 (源代码)
content = response.read().decode()

# 6.保存一页到本地,看展示效果
with open('1.html','w',encoding='utf-8') as file:
    file.write(content)