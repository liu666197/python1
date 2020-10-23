# 正则的模块
import re

a = ',mAa1232wabcWwqew1232qewewqew21331weer'

result = re.search('[aw]',a)
# 数字
result = re.search('[0123456789]',a)
result = re.search('[0-9]',a)
# 字母
result = re.search('[a-z]',a,re.I)
# 数字和字母
result = re.search('[a-z0-9A-Z]',a,re.I)

result = re.search('[^0-9]',a)
# 另外一个或者
result = re.search('0|1|a',a)
# 量词
#5个
result = re.search('[0-9]{5}',a)
result = re.search('[a-z]{5}',a)
# 大于等于n个
result = re.search('[a-z]{1,}',a)
result = re.search('[a-z]{0,}',a)
a = '1,mAa1232wab cWwqew1232qewewqew21331weer'
# n-m个
result = re.search('[a-z]{3,6}',a)
# 数字
result = re.search('\d{1,}',a)
result = re.search('\D{1,}',a)
# 数字字母下划线
result = re.search('\w{1,}',a)
result = re.search('\W{1,}',a)
# 空格
result = re.search('\s{1,}',a)
result = re.search('\S{1,}',a)
# 量词的符号
result = re.search(r'\d*',a)
result = re.search(r'\d+',a)
result = re.search(r'\d?',a)
a = '1,m?Aa.1232wab\ncWwqew1232qewewqew21331weer'
# .: 匹配除了换行之外的任意字符
result = re.search(r'.+',a,re.S)
# 想匹配.的位置
result = re.search(r'\.',a)
result = re.search(r'\?',a)

a = 'hello world'
# 开头结尾
result = re.search(r'^a',a)
result = re.search(r'd$',a)
# 开头和结尾一起使用的时候,匹配到的是^和$中间的内容
result = re.search(r'^hello world$',a)
print(result)




#
# # result = re.match('122',a)
# # print(result)
# result = re.search('w',a,re.I)
# # 从查找的对象中取出结果
# print(result)
# print(result.span())