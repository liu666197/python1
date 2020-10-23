import re
a = '<a href="#">新闻</a><a href="#">hao123</a>'
# 从a里面把新闻两个字提取出来
# findall结合括号使用: 括号代表要匹配的结果
# 贪婪模式: 匹配到越多越好
# pattern = r'<a href="#">(.+)</a>'
#非贪婪模式: 每次匹配的时候,匹配到第一个符号条件的内容就结束
pattern = r'<a href="#">(.+?)</a>'

result = re.findall(pattern,a)
print(result)

a = '''
<a href="http://news.baidu.com" target="_blank" class="mnav c-font-normal c-color-t">新



闻</a>
<a href="https://www.hao123.com" target="_blank" class="mnav c-font-normal c-color-t">hao123</a>
<a href="#">sadjklasdasjkld</a>
'''
# 规则
# pattern = r'<a href=".+?" target="_blank" class="mnav c-font-normal c-color-t">(.+?)</a>'
pattern = r'class="mnav c-font-normal c-color-t">(.+?)</a>'
# re.S:
result = re.findall(pattern,a,re.S)
print(result)