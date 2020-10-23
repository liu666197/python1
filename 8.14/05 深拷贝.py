import copy
a = [{'name': 'zs'},{'name': 'lisi'}]
# 深拷贝
b = copy.deepcopy(a)
b[0]['name'] = '张三'
# a和b会影响
print('a:',a)
print('b:',b)