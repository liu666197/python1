import requests
userInput = input('输入要翻译的内容: ')
url = 'https://dict.iciba.com/dictionary/word/suggestion?nums=5&ck=709a0db45332167b0e2ce1868b84773e&timestamp=1598234096722&client=6&uid=123123&key=1000006&is_need_mean=1&signature=bd609d96e3fb89632b9bb062869f1a75'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
dic = {
    'word': userInput
}
response = requests.get(url,headers = headers,params=dic)
result = response.json()['message'][0]['means'][0]['means']
result = ','.join(result)
print(result)