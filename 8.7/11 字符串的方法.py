a = 'hello world hello aaa'

# a += '1'
# print(a)
# 查
# 查找字符串出现的次数
# result = a.count(' ')
# 查找字符串的下标: 默认查找到第一个的下标 (查找不到报错)
# result = a.index('worlds')
# 从右往左查
# result = a.rindex('hello')
# 查找不到为-1,不会报错
# result = a.find('hello')
# 从右往左查
# result = a.rfind('hellso')
# print(result)
# 内容替换(默认全部替换)
# b = a.replace('hello','你好')
# 替换掉一下 (替换几个)
# a = a.replace('hello','你好',1)
# print(a)
a = 'hello World hello aaa'
# 字母大小写
# 大写
# b = a.upper()
# 小写
# b = a.lower()
# 每个首字母大写
# b = a.title()
# 第一个单词首字母大写
# b = a.capitalize()
# 字母大小写取反
# b = a.swapcase()
# print(b)
# 去除首尾空格
# a = '         hello World hello aaa       '
# a = a.strip()
# print(a)
# 字符串的对齐
# a = 'hello'
# # 字符串在11个字符的宽度里面居中对齐
# b = a.center(11)
# # 字符串在11个字符的宽度里面左对齐
# b = a.ljust(11)
# # 字符串在11个字符的宽度里面右对齐
# b = a.rjust(11)
#
# print(111,b,222)

# 字符串和列表的转换
# a = 'hello+world hello aaa'
# # 字符串转化为列表
# # 默认按照空格分割
# # b = a.split()
# b = a.split('+')
# print(b)

# 列表-->字符串
# a = ['hello','world','你好','世界']
# # 按照一个字符将列表转化为字符串
# b = '?'.join(a)
# print(b)
# a = 'hello world'
# a = '123213.1'
# # is开头的表示判断
# # 是否大写
# b = a.isupper()
# # 是否小写
# b = a.islower()
# # 是否为数字(整数)
# b = a.isdecimal()
# print(b)

# 字符和ASCII的转换
# 二进制数值: 01010110101
# 字母: ABCDE
# ASCII值: 字母的数字表示方式

# ord() : 将字母转化为ASCII值
# chr() : 将ASCII转化为字母
# 小写字母的ASCII值与大写的ASCII差32
print(ord('A'))# 65
print(ord('a'))# 97
print(chr(65))
print(chr(97))