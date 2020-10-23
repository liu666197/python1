# 1. 计算从1到1000以内所有能被3或者17整除的数的和并输出
# sum = 0
# num = 1
# while num <= 1000:
#     if num % 3 == 0 or num % 17 == 0:
#         print(num)
#         sum += num
#     num += 1
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

# 6.五位数中，对称的数称为回文数，打印所有的回文数并计算个数。如:12321

# 原理: 拿到所有的五位数,获得个十百千万的数字,如果第一位和倒数第一位相同,第二位和倒数第二位相同,就是回文数

# 7.公园里有一只猴子和一堆桃子，猴子每天吃掉桃子总数的一半，把剩下一半中扔掉一个坏的。到第七天的时候，猴子睁开眼发现只剩下一个桃子。问公园里刚开始有多少个桃子？
# 总

# class student:
#     def __init__(self,age,name,nianji):
#         self.name=name
#         self.age=age
#         self.nianji=nianji
#         def study(self):
#             print ( self.name+'在学习')
#         def rest(self):
#             print (self.name +'在休息')
#






