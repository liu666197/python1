# 必要(位置)参数
# def sayHello(a):
#     print('hello',a)
#
# sayHello(10)
# a = []
# a.sort(reverse=False)
# 默认参数
# def sayHello(a = 10):
#     print('hello',a)
# sayHello(20)

# 混合参数: 必要参数 + 默认参数
# def sayHello(a,b = 30):
#     print('hello',a,b)
# sayHello(20,40)
# def sayHello(a,b):
#     print('hello',a,b)
# # 关键字参数 (针对于实参的传递来说) 直接指定实参的值传递给哪个形参
# sayHello(b = 10,a = 20)
# 不定长参数
# def sayHello(*args):
#     print('hello')
#     print(args)

# 不定长关键字参数 (keyword)
# def sayHello(**kwargs):
#     print('hello',kwargs)
# sayHello(a = 20,b = 10,c = 30,d = 40,e = 50,f = 60)

def sayHello(*args,**kwargs):
    print(args,kwargs)

sayHello(10,20,304,404,a = 20,n = 40,b = 40)



# sayHello([10,20,30],20,39,40,50,70)

# python的内置函数
# 传递多个参数
# a = max(10,20,30,405,213,32,345,3254,345,46,45,654)
# a = max([213,234,324,3])
# a = max([123,234,23,4],234,23,43,[123,123,21,312,32,1],534,5,45,4)
# # print(a)
#
# # a = min(10,20,30,405,213,32,345,3254,345,46,45,654)
# a = min([213,234,324,3])
# print(a)
