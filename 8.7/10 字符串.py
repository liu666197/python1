# 字符串: 一堆的字符(单个内容)组成
a = 'hello world'
# 通过下标取字符
print(a[0])
# 不能修改字符串里面的字符
# a[0] = 'a'
print(len(a))
# 遍历字符串
# 通过下标遍历
for i in range(len(a)):
    print(a[i])
# 直接遍历字符
for i in a:
    print(i)