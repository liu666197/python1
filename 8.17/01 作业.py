# def puke(a,b):
#     # [('红心','A'),('草花','A'),...,('方块','K'),('黑桃','K')]
#     result = [(y,i) for i in b for y in a]
#     return result
# print(puke(['红心','草花','方块','黑桃'],['A','2','3','4','6','7','8','9','10','J','Q','K']))
# 1.编写一个函数cacluate, 可以接收任意多个数,返回的是一个元组.
# 元组的第一个值为所有参数的平均值, 第二个值是大于平均值的所
# 有数.(2.5,(3,4))
def cacluate(*args):
    # sum = 0
    # for i in args:
    #     sum += i
    aver = sum(args) / len(args)
    a = []
    for i in args:
        if i > aver:
            a.append(i)
    return (aver,a)


# print(cacluate(1,2,3,4))

# 2.编写一个函数, 接收字符串参数, 返回一个元组,‘ehllo WROLD’
# 元组的第一个值为大写字母的个数, 第二个值为小写字母个数.
def f(a):
    upper_count = 0
    lower_count = 0
    for i in a:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
    # return (upper_count,lower_count)
    return upper_count,lower_count
# print(f('ehllo WROLD'))

# 3.编写函数, 接收一个列表(包含30个1~100之间的随机整形数)和一
# 个整形数k, 返回一个新列表.
# 函数需求:
# - 将列表下标k之前对应(不包含k)的元素逆序;
# - 将下标k及之后的元素逆序;
# [1,2,3,4,5] 2 [2,1,5,4,3]
# def f(a,k):
#     return a[k - 1::-1] + a[:k - 1:-1]
# print(f([1,2,3,4,5],2))
# print((lambda a,k:a[k - 1::-1] + a[:k - 1:-1])([1,2,3,4,5],2))

# 4.腾讯笔试题:
# 题目需求:
# 	f(n): 返回n里面的每一位数字的平方和
#     对于一个十进制的正整数， 定义f(n)为其各位数字的平方和，如:
#     f(13) = 1**2 + 3**2 = 10
#     f(207) = 2**2 + 0**2 + 7**2 = 53
#     下面给出三个正整数k，a, b,你需要计算有多少个正整数n满足a<=n<=b,
#     且k*f(n)=n
# 输入:
#     第一行包含3个正整数k，a, b, k>=1,  a,b<=10**18, a<=b;
# 输出：
#     输出对应的答案;
#
# 范例:
#     输入: 51 5000 10000
#     输出: 3 (这些数字n具体是哪些)
# 求平方和
def f(n):
    sum = 0
    for i in str(n):
        sum += int(i) ** 2
    return sum
userInput = [int(i) for i in input('输入: ').split(' ')]
k = userInput[0]
a = userInput[1]
b = userInput[2]
count = 0
for n in range(a,b + 1):
    if k * f(n) == n:
        count += 1
        # print(n)
print(count)













