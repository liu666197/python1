
# 值传递: 数字或者字符串
# a = 10
# def sayHello(b): # b = 10
#     b = 20
#     print('函数里面的b:',b)
# sayHello(a)
# print('函数外面的a:',a)

# 引用传递: 对象
a = [10,20,30]
def sayHello(b):
    b[0] = 200
    print('函数里面的b',b)
sayHello(a)
print('函数外面的a:',a)
