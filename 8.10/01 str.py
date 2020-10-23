# a = 10
# # 错误
# str = 'sdasda'
# b = str(a)
# print(a)

# a = ['hello','world','你好','10']
# # 'hello' + ',' +'world' + ','+ '你好' + ',' + 10
# b = ','.join(a)
# print(b)
#
# a = 'hello'
# b = a.center(11,'?')
# b = a.ljust(11,'?')
#
# print('++++',b,'-----')
# 字符串 --> 列表
a = 'hello world'
# b = []
# for i in a:
#     b.append(i)
# print(b)
b = list(a)
print(b)
# print('' in a)
# 默认是空格 不允许放空字符串
# b = a.split('')
# print(b)
# a = '    hello    '
# print(a)
# a = '++++hello++++'
# b = a.strip()
# print(b)

# 格式化字符串: 让字符串按照某种格式输出  字符串.format(变量,变量,变量)
a = 10
b = 20
# print('a的值是%s,b的值是%s'%(a,b))
print('a的值是{},b的值是{}'.format(a,b))