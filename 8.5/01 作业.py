# # 0.实现简易计算器功能
# a = int(input('第一个数: '))
# b = int(input('第二个数: '))
# # or运算一般会用来作为默认值使用
# c = input('输入要运算的符号(+,-,*,/): ') or '+'
# if c == '+':
#     print(a + b)
# if c == '-':
#     print(a - b)
# if c == '*':
#     print(a * b)
# if c == '/':
#     print(a / b)
# else:
#     print('输入正确的符号')
# if c == '':
#     print(a + b)
# 1.让用户输入两个任意的整数, 比较两个数的大小, 输出最大的数
# a = int(input('第一个数: '))
# b = int(input('第二个数: '))
# if a > b:
#     print('最大值为: %s'%(a))
# else:
#     print('最大值为: %s' % (b))
# 12.让用户输入三个任意的整数, 比较三个数的大小, 输出最大的数
# a = int(input('第一个数: '))
# b = int(input('第二个数: '))
# c = int(input('第三个数: '))
# # 假设第一个数就是最大值
# max = a
# if b > max:
#     max = b
# if c > max:
#     max = c
# print('最大值是',max)
# 2.用户输入一个数,打印出奇数还是 偶数 (余数是否为0)
# a = int(input('第一个数: '))
# if a % 2 == 0:
#     print('偶数')
# else:
#     print('奇数')
# 3.用户输入帐号密码,帐号为admin,密码为8888显示登录成功,其余的显示登录失败
# id = input('请输入账号: ')
# pwd = input('请输入密码: ')
# if id == 'admin' and pwd == '8888':
#     print('登录成功')
# else:
#     print('登录失败')
# 4.用户输入一个三位数,输出结果是否为水仙花数(水仙花数: 水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。)
# a = int(input('请输入一个三位数: '))
# # 思路: 将每一位数字取出来,相加即可
# # 百位
# bai = a // 100
# # 十位
# shi = a // 10 % 10
# # 个位
# ge = a % 10
# # 结果
# result = bai ** 3 + shi ** 3 + ge ** 3
# if result == a:
#     print('水仙花数')
# else:
#     print('不是水仙花数')
#5.用户输入年份,输出结果是闰年还是平年(闰年: 1.能整除4且不能整除100 2.能整除400)
# year = int(input('输入年份: '))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('闰年')
# else:
#     print('平年')
# 6.输入公交卡当前的余额,空座位数，只要超过2元，就可以上公交车;没钱,撵走；如果空座位的数量大于0，就可以坐下;
# money = int(input('请输入当前余额: '))
# if money >= 2:
#     seat = int(input('输入座位数: '))
#     if seat > 0:
#         print('坐下')
#     else:
#         print('站着吧!!!')
# else:
#     print('撵走')
# 7.成绩等级:
# 	90分以上:  等级为A
#
# 	80-90: 等级为B
#
# 	60-80: 等级C
#
# 	0-60: 等级为D
score = int(input('输入成绩: '))
if  score >= 90:
    print('A')
if score >= 80 and score < 90:
    print('B')
if score >= 60 and score < 80:
    print('C')
if score >= 0 and score < 60:
    print('D')

# 8.场景应用: 上火车 (用户输入表示是否有票,是否有刀具)
# 	是否有票,有票打印可以进站;
# 	进站查看是否带有刀具,有刀具,没收上车,没有刀具,直接上车
# 	没票打印不可以进站
# 票
# tickets = input('输入是否有票: ')
# if tickets == '是':
#     print('进站')
#     # 刀具
#     knife = input('是否有刀具: ')
#     if knife == '是':
#         print('没收,上车')
#     else:
#         print('直接上车')
# else:
#     print('不能进站')
# 9.女友的节日:
# 	定义holiday_name字符串变量记录节日名称
# 	如果是 情人节 应该 买玫瑰／看电影
# 	如果是 平安夜 应该 买苹果／吃大餐
# 	如果是 生日 应该 买蛋糕
# 	其他的时候,每天都是节日
holiday_name = input('输入名称: ')
if holiday_name == '情人节':
    print('买玫瑰／看电影')
    exit()
if holiday_name == '平安夜':
    print('买苹果／吃大餐')
    exit()
if holiday_name == '生日':
    print('买蛋糕')
    exit()
else:
    print('每天都是节日')

# 10.英雄联盟(LOL)李青技能:
# 	q,Q:天音波
# 	w,W:金钟罩/铁布衫
# 	e,E:天雷破/摧筋断骨
# 	r,R:猛龙摆尾
# 技能
# skill = input('输入技能: ')
# if skill in 'qQ':
#     print('天音波')
# if skill in 'wW':
#     print('金钟罩/铁布衫')
# if skill in 'eE':
#     print('天雷破/摧筋断骨')
# if skill == 'q' or skill == 'Q':
#     print('天音波')
# if skill == 'w' or skill == 'W':
#     print('金钟罩/铁布衫')
# if skill == 'e' or skill == 'E':
#     print('天雷破/摧筋断骨')

# 11.用户决定是否发工资,工资数是多少,信用卡欠款;有剩余的时候,显示剩余金额(图1)
# isSalary = input('是否发工资: ')
# if isSalary == '是':
#     # 工资
#     salary = int(input('输入工资数: '))
#     # 信用卡
#     IDcard = int(input('输入信用卡欠款: '))
#     # 余额
#     balance = salary - IDcard
#     if balance > 0:
#         print('又可以happy了')
#     else:
#         print('No')
# else:
#     print('盼工资')




