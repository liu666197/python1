# a = [123,123,12]
# print(type(a) == list)
# print(isinstance(a,list))
class A:
    pass
class B(A):
    pass

a = A()
print(a)

b = B()
print(b)
# 判断对象a是否由A类创建
# print(type(a) == A)
# print(type(a) == B)
# print(isinstance(a,A))
# print(isinstance(a,B))

# print(type(b) == B)
# print(type(b) == A)

# print(isinstance(b,B))
print(isinstance(b,A))