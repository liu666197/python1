import re

with open('test.html','r',encoding='utf-8') as file:
    content = file.read()
# 第一条数据的所有代码
# print(content)
# 规则
pattern = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
# findall (从第一条数据的所有代码找)
result = re.findall(pattern,content,re.S)
print(result[0][1],result[0][2])

# 人气数
pattern = r'<span class="statistics-view" title="共(.+?)人气">'
fansResult = re.findall(pattern,content,re.S)
print(fansResult[0])