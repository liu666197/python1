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

# 该循环从2-100
num = 2
while num <= 100:
    count = 2
    # 该循环如果能正常结束,就代表该数字是一个质数
    while count < num:
        # 能整除,就代表不是质数,如果都不能整除,就代表是质数
        if num % count == 0:
            # print('%s不是质数' % (num))
            break
        count += 1
    else:
        # 循环正常结束的时候,会执行该else里面的代码
        # print('%s是质数' % (num))
        print(num,end='\t')
    num += 1

