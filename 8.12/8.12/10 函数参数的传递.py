# 全局变量
# a = 10
# def sayHello():
#     # 定义变量 (局部变量)
#     # a = 10
#     print('函数里面的a:',a)
# sayHello()
# print('函数外面的a:',a)

a = 10
def sayHello():
    # 声明a变量是全局变量即可
    global a
    a = 20
    print('函数里面的a:', a)
sayHello()
print('函数外面的a:',a)