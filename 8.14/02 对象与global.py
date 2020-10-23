# 只要将对象赋值了,那么就会开辟新的空间来存储对象
# a = []
# # 是否属于改变了a变量的值??? 都不是改变了a的值
# a.append(1)
# a[0] = 2
# print(a)
# b = []
# print(id(a),id(b))
# a存储的是列表的内存地址
a = [10,20,30]
b = 20
def sayHello():
    global b
    b = 30
    a[0] = 100
    print(b)
sayHello()
print(b)
print(a)