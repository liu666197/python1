# 不影响
# a = [10,20,30]
# # a = [{'name': 'zs'},{'name': 'lisi'},{'name': 'wangwu'}]
# b = a.copy()
# b[0] = 100
# # a和b互不影响
# print('a:',a)
# print('b:',b)

# 对象的嵌套
a = [{'name': 'zs'},{'name': 'lisi'}]
b = a.copy()
b[0]['name'] = '张三'
# a和b会影响
print('a:',a)
print('b:',b)