# a = [123,21,3423,4,324,234]
# 从小到大排序
# a.sort()
# a.sort(reverse=True)
# 不会使列表本身发生变化,函数的返回值就是排序后的内容
# result = sorted(a,reverse=True)
#
# print(a)
# print(result)

a = [
    {'name': 'zs1','age': 30},
    {'name': 'zs32','age': 50},
    {'name': 'zs12','age': 10},
    {'name': 'zsqew','age': 20},
    {'name': 'zs213','age': 100},
    {'name': 'zswer','age': 3}
]
# n: 代表列表中的每个元素
def f(n):
    return n['name']
# 按照年龄进行排序
result = sorted(a,key=f)
print(result)


# def sayHello():
#     print('hello')
#
# print(sayHello)



# # 选择排序
# for i in range(len(a)):
#     for j in range(i + 1,len(a)):
#         if a[i]['age'] > a[j]['age']:
#             a[i],a[j] = a[j],a[i]
# print(a)