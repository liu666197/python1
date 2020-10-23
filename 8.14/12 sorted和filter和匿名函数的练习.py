a = [
    {'name': 'aa','age': 80},
    {'name': 'zs1','age': 30},
    {'name': 'aasd32','age': 50},
    {'name': 'zs12','age': 10},
    {'name': 'zsaqew','age': 20},
    {'name': 'zs213','age': 100},
    {'name': 'zswer','age': 3}
]
# 1.使用def的函数的方式,取出大于20的数据,并且从小到大排序

def f(n):
    return n['age'] > 20
def f1(n):
    return n['age']

a = list(filter(f,a))
# a = list(filter(lambda n:n['age'] > 20,a))
# a = sorted(a,key=lambda n:n['age'])
# print(a)
# 2.使用匿名函数的方式,取出名字带有字母a的数据,并且从小到大排序
a = list(filter(lambda  n:'a' in n['name'],a))
a = sorted(a,key=lambda n:n['age'])
print(a)