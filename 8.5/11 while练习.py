# 练习:
# 1.打印1-100
# count = 1
# while count < 101:
#     if count % 2 == 0:
#         print(count)
#     count += 1
# 2.打印1-100的偶数
# count = 2
# while count <= 100:
#     print(count)
#     count += 2
# 3.求出1-100的和 : 1+2+3+...+99+100

# 和: 银行卡余额: 0 salary
# 第一个月工资: 1  salary += 1
# 第二个月工资: 2  salary += 2
# 第三个月工资: 3 salary += 3  salary += 100
# 和
# sum = 0
# count = 1
# while count <= 100:
#     if count % 2 == 0:
#         sum += count
#     count += 1
# print(sum)

# 4.求出1-100的偶数和

# *
# **
# ***
# ****
# *****
count = 1
while count <= 5:
    print(count * '*')
    count += 1
# print('*' * 1)
# print('*' * 2)
# print('*' * 3)
# print('*' * 4)
# print('*' * 5)
# *
# ***
# *****
# *******
# *********
# 1-9的数
# count = 1
# while count <= 9:
#     print(count * '*')
#     count += 2
# *
# ***
# *****
# *******
# *********
# *******
# *****
# ***
# *
count = 1
while count <= 9:
    print(count * '*')
    count += 2

# 获取到7,5,3,1
count = 7
while count > 0:
    print(count * '*')
    count -= 2