# 1. 计算从1到1000以内所有能被3或者17整除的数的和并输出
# sum = 0
# num = 1
# while num <= 1000:
#     if num % 3 == 0 or num % 17 == 0:
#         print(num)
#         sum += num
#     num += 1
# print(sum)
# sum = 0
# for num in range(1,1001):
#     if num % 3 == 0 or num % 17 == 0:
#         sum += num
# print(sum)


# 2. 求1到10的阶乘 (格式为 5的阶乘为: 120 )
# 1 : 1
# 2 : 2 * 1
# 3 : 3 * 2 * 1
# 4 : 4 * 3 * 2 * 1
# num = 1
# # 乘积: 从1开始
# result = 1
# while num <= 10:
#     result *= num
#     print('%s的阶乘为: %s'%(num,result))
#     num += 1
# result = 1
# for num in range(1,11):
#     result *= num
#     print('%s的阶乘为: %s' % (num, result))
# 打印的时候从大往小打印
# 先算10的阶乘
# num = 1
# # 阶乘结果
# result = 1
# while num <= 10:
#     result *= num
#     num += 1
# print('%s的阶乘为: %s'%(num - 1,result))
# # 再算后面每一个的阶乘
# num = 9
# while num > 0:
#     result /= (num + 1)
#     print('%s的阶乘为: %s' % (num, int(result)))
#     num -= 1

# 3. 求一到十阶乘之和。(1: 1 2: 2  3: 6  4: 24 5: 120)

# num = 1
# # 乘积: 从1开始
# result = 1
# sum = 0
# while num <= 10:
#     result *= num
#     sum += result
#     num += 1
# print(sum)
# sum = 0
# result = 1
# for num in range(1,11):
#     result *= num
#     sum += result
# print(sum)

# 4. 功能：用户登录(三次机会尝试)
# 用户名密码：
# name = "aaa"
# password = "123"
# 让用户输入，如果输入正确，显示登录成功， 失败，显示还有几次机会， 超过三次失败，显示失去登录机会，明天再来。退出程序。
# count = 3
# while count > 0:
#     name = input('请输入用户名: ')
#     password = input('请输入密码: ')
#     # 只要输入了,次数减-1
#     count -= 1
#     if name == 'aaa' and password == '123':
#         print('登录成功')
#         # 登录成功,终止循环
#         break
#     else:
#         if count == 0:
#             print('失去登录机会，明天再来。')
#         else:
#             print('登录失败,还有%s次机会'%(count))

# for count in range(2,-1,-1):
#     name = input('请输入用户名: ')
#     password = input('请输入密码: ')
#     if name == 'aaa' and password == '123':
#         print('登录成功')
#         break
#     else:
#         if count == 0:
#             print('失去登录机会，明天再来。')
#         else:
#             print('登录失败,还有%s次机会' % (count))

# 5. 打印出所有的“水仙花数”。
# 所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方+5的三次方+3的三次方。
# num = 100
# while num < 1000:
#     # 个位
#     ge = num % 10
#     # 十位
#     shi = num // 10 % 10
#     # 百位
#     bai = num // 100
#     result = ge ** 3 + shi ** 3 + bai ** 3
#     if num == result:
#         print(num)
#     num += 1

# for num in range(100,1000):
#     # 个位
#     ge = num % 10
#     # 十位
#     shi = num // 10 % 10
#     # 百位
#     bai = num // 100
#     result = ge ** 3 + shi ** 3 + bai ** 3
#     if num == result:
#         print(num)

# 6.五位数中，对称的数称为回文数，打印所有的回文数并计算个数。如:12321

# 原理: 拿到所有的五位数,获得个十百千万的数字,如果第一位和倒数第一位相同,第二位和倒数第二位相同,就是回文数

# 7.公园里有一只猴子和一堆桃子，猴子每天吃掉桃子总数的一半，把剩下一半中扔掉一个坏的。到第七天的时候，猴子睁开眼发现只剩下一个桃子。问公园里刚开始有多少个桃子？
# 总
# all = 1
# # 天数
# day = 6
# while day > 0:
#     all = (all + 1) * 2
#     # print('第%s天,剩下了%s的桃子'%(day,all))
#     day -= 1
# print('桃子总数为: %s'%(all))
# all = 1
# for day in range(6,0,-1):
#     all = (all + 1) * 2
# print(all)
# 1.输出9行内容，第1行输出1，第2行输出12，第3行输出123，以此类推，第9行输出123456789
#
# 1
# 12
# 123
# 1234
# 12345
# 123456
# 1234567
# 12345678
# 123456789

# 输出123
# print(1,end='')
# print(2,end='')
# print(3,end='')
# num = 1
# while num <= 3:
#     print(num,end='')
#     num += 1
# for num in range(1,4):
#     print(num,end='')
# print()
# for num in range(1,7):
#     print(num,end='')
# print()
# for count in range(2,11):
#     for num in range(1, count):
#         print(num, end='')
#     print()
# # 单独的换行
# print()
#
# # 输出123456
# num = 1
# while num <= 6:
#     print(num,end='')
#     num += 1
# print()
# # 输出123456789
# num = 1
# while num <= 9:
#     print(num,end='')
#     num += 1
# print()
#
# count = 1
# while count <= 9:
#     num = 1
#     while num <= count:
#         print(num, end='')
#         num += 1
#     print()
#     count += 1

# 2.打印菱形
#    *                  第一行:  ' ' * 3,'*' * 1
#   ***                 第二行:  ' ' * 2,'*' * 3
#  *****                第三行:  ' ' * 1,'*' * 5
# *******               第四行:  ' ' * 0,'*' * 7
#  *****                             * 1,      5
#   ***                                2,      3
#    *                                 3,      1
# 星号数
# count = 1
# for spaceCount in range(3,-1,-1):
#     print(' ' * spaceCount,end="")
#     print('*' * count)
#     count += 2
#
# count = 5
# for spaceCount in range(1,4):
#     print(' ' * spaceCount, end="")
#     print('*' * count)
#     count -= 2

# 空格个数
# spaceCount = 3
# # *个数
# count = 1
# while spaceCount >= 0:
#     print(spaceCount * ' ',end='')
#     print(count * '*')
#     spaceCount -= 1
#     count += 2
# spaceCount = 1
# count = 5
# while spaceCount <= 3:
#     print(spaceCount * ' ',end='')
#     print(count * '*')
#     spaceCount += 1
#     count -= 2

# 3.打印九九乘法表
# 1 * 1 = 1
# 1 * 2 = 2	2 * 2 = 4
# 1 * 3 = 3	2 * 3 = 6	3 * 3 = 9
# 1 * 4 = 4	2 * 4 = 8	3 * 4 = 12	4 * 4 = 16
# 1 * 5 = 5	2 * 5 = 10	3 * 5 = 15	4 * 5 = 20	5 * 5 = 25
# 1 * 6 = 6	2 * 6 = 12	3 * 6 = 18	4 * 6 = 24	5 * 6 = 30	6 * 6 = 36
# 1 * 7 = 7	2 * 7 = 14	3 * 7 = 21	4 * 7 = 28	5 * 7 = 35	6 * 7 = 42	7 * 7 = 49
# 1 * 8 = 8	2 * 8 = 16	3 * 8 = 24	4 * 8 = 32	5 * 8 = 40	6 * 8 = 48	7 * 8 = 56	8 * 8 = 64
# 1 * 9 = 9	2 * 9 = 18	3 * 9 = 27	4 * 9 = 36	5 * 9 = 45	6 * 9 = 54	7 * 9 = 63	8 * 9 = 72	9 * 9 = 81

# 1 * 2 = 2	2 * 2 = 4
# 第二行
# row = 2
# # print('%s * %s = %s'%(1,row,1 * row),end='\t')
# # print('%s * %s = %s'%(2,row,2 * row),end='\t')
# count = 1
# while count <= row:
#     print('%s * %s = %s' % (count, row, count * row), end='\t')
#     count += 1
# print()
# 第二行
# row = 5
# for count in range(1,row + 1):
#     print('%s * %s = %s' % (count, row, count * row), end='\t')
# print()
# row = 9
# for count in range(1,row + 1):
#     print('%s * %s = %s' % (count, row, count * row), end='\t')
# print()

# for row in range(1,10):
#     for count in range(1, row + 1):
#         print('%s * %s = %s' % (count, row, count * row), end='\t')
#     print()
#
# # 第四行
# row = 3
# count = 1
# while count <= row:
#     print('%s * %s = %s' % (count, row, count * row), end='\t')
#     count += 1
# print()
# 行数
# row = 1
# while row <= 9:
#     count = 1
#     while count <= row:
#         print('%s * %s = %s' % (count, row, count * row), end='\t')
#         count += 1
#     print()
#     row += 1

# 4.求出1-100所有的质数(质数: 只能被1和它本身整除的数)
# 	9: 2,3,4,5,6,7,8
#
# 	6: 2,3,4,5

# # 判断9是不是质数
# num = 13
# count = 2
# # 该循环如果能正常结束,就代表该数字是一个质数
# while count < num:
#     # 能整除,就代表不是质数,如果都不能整除,就代表是质数
#     if num % count == 0:
#         print('%s不是质数'%(num))
#         break
#     count += 1
# else:
#     # 循环正常结束的时候,会执行该else里面的代码
#     print('%s是质数'%(num))

# 判断9
# num = 11
# for count in range(2,9):
#     if num % count == 0:
#         # 不是质数,直接退出
#         break
# else:
#     print('%s是质数'%(num))

for num in range(2,101):
    for count in range(2, num):
        if num % count == 0:
            # 不是质数,直接退出
            break
    else:
        print(num,end='\t')

# 该循环从2-100
# num = 2
# while num <= 100:
#     count = 2
#     # 该循环如果能正常结束,就代表该数字是一个质数
#     while count < num:
#         # 能整除,就代表不是质数,如果都不能整除,就代表是质数
#         if num % count == 0:
#             # print('%s不是质数' % (num))
#             break
#         count += 1
#     else:
#         # 循环正常结束的时候,会执行该else里面的代码
#         # print('%s是质数' % (num))
#         print(num,end='\t')
#     num += 1
#



