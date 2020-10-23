# 有名字的函数
def sayHello(n):
    return n ** 2
print(sayHello(100))
# 求和
def sum(a,b):
    return a + b

# 匿名: 没有名字的函数
print((lambda n:n ** 2)(10))
a = lambda n:n ** 2
print(a(10))
# 求和
print((lambda a,b:a + b)(10,20))

# lambda n:n[0::2]

def b(n):
    if len(n) > 5:
        return n[:6]

# print((lambda n:n[:6])([1,2,3]))

a = lambda n:n[:6] if len(n) > 5 else 1
print(a([1,2,3,2343,2,423,42]))

print((lambda n:n[:6] if len(n) > 5 else 1)([123,12,312,312,31]))