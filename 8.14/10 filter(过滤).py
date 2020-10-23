a = [
    {'name': 'zs32','age': 80},
    {'name': 'zs1','age': 30},
    {'name': 'zs32','age': 50},
    {'name': 'zs12','age': 10},
    {'name': 'zsqew','age': 20},
    {'name': 'zs213','age': 100},
    {'name': 'zswer','age': 3}
]
def f(n):
    # 筛选条件
    return n['age'] >= 50

# 取出年龄大于50岁的数据
result = list(filter(f,a))

print(result)