# 1-100的列表
# a = list(range(101))
# print(a)
# a = []
# for i in range(101):
#     a.append(i)
# print(a)
# 列表生成式: 格式: [列表中的元素 for 变量 in 序列]
a = [i for i in range(1,101)]
# 1-100列表 (字符串类型的'1' - '100')
a = [str(i) for i in range(1,101)]
print(a)
a = [10,123,23,423,432,423]
a = [i + 1 for i in a]
a = [1,2,3,4,5] # [1,4,9,16,25]
a = [i ** 2 for i in a]
print(a)

# 和if使用: [列表中的元素 for 变量 in 序列 if 条件]
a = [10,20,30,123,2,423,43,24,3224]
# 去除偶数
# a = [i for i in a if i % 2 != 0]
# 大于50的数字
a = [i for i in a if i >= 50]
print(a)
# a = list(range(1,101))
# for i in range(len(a)):
#     a[i] += 1
# print(a)
# 和if else使用: [列表中的元素 if 条件  else 列表中的元素 for 变量 in 序列]
a = [1,2,3,4]  # [1,4,27,16]

a = [i ** 2 if i % 2 == 0 else i ** 3 for i in a]
# 偶数-->平方 奇数-->立方
print(a)

a = [1,2,3,4]
b = [5,6,7,8]

c = [[i,y] for i in a for y in b]
print(c)
# for i in a:
#     for y in b:
#