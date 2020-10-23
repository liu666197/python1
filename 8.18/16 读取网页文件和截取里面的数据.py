import re
# 1.读取网页文件的内容
with open('百度.html','r',encoding='utf-8') as file:
    content = file.read()

# 2.分析我们需要的数据的代码的结构
pattern = r'class="mnav c-font-normal c-color-t">(.+?)</a>'

# 3.从源代码当中查找出所有内容
result = re.findall(pattern,content,re.S)
print(result)
