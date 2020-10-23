# 比名片系统难一些(所有知识点的整合,列表,字符串,字典,函数)
#
# 双色球彩票系统: 6个功能全部封装成函数.
#
# # 自己的余额自己设置
# price = 10000
#
# [{'red': 红球列表,'blue': 蓝球},{'red': 红球列表,'blue': 蓝球}]
#
# 彩票: {
# 	'red': [],
# 	'blue': int
# }
#
# 一张彩票:
# {'red': [],'blue': int}
#
# 所有的彩票:[{'red': [],'blue': int},{'red': [],'blue': int},{'red': [],'blue': int},{'red': [],'blue': int},{'red': [],'blue': int}]
#
#
# - 从1-33共33个红色号码球中选择6个号码，并从1-16共16个蓝色号码球中选择1个号码
#
#
# - 交互大框架 （原始金额自定，彩票2元一张）
import random
# 提示内容
msg = '''==================================================
   双色球 V0.01
 1. 充值  （先显示原有金额，再输入金额，最后显示充值后的金额）
 2. 随机生成一个彩票 (显示生成的彩票: 红球: 12... 蓝球: 蓝球号码)
 3. 手动输入彩票号码(总共输入7个号码,每个号码中间逗号隔开,前六个是红球号码,最后一个是蓝球号码): 1,2,3,4,5,6,7
 4.查看最新一期彩票结果, 显示开奖后的账户余额 （最新一期彩票结果随机产生）
 5. 显示当前余额
 6. 显示所有的彩票:
 7.	退出系统
=================================================='''
print(msg)
# 余额
balance = 10000000
# 所有的彩票
allTickets = []
# 充值
def addMoney(money):
    global balance
    balance += money
    print('充值成功')
    print('充值后的金额为: %s'%(balance))

# 显示当前余额
def showBalance():
    print('当前余额为: %s'%(balance))

# 随机生成一张彩票 (中奖的彩票也是随机生成的)
def randomTicket():
    # {'red': [6个1-33的数字],'blue': 1-16}
    # random.sample(列表,n) : 从列表里面取出n个不重复的数字
    # 1-33的红球列表
    redList = list(range(1,34))
    # 取出6个数 (红球)
    red = random.sample(redList,6)
    # 蓝球
    blue = random.randint(1,16)
    dic = {'red': red,'blue': blue}
    return dic

# 随机购买一张彩票
def randomBuyTicket():
    global balance
    # 判断余额支不支持购买彩票
    if balance >= 2:
        # 随机生成彩票
        dic = randomTicket()
        # 判断现在生成的彩票是否已经存在在列表当中
        # 把生成的彩票放入allTickets里面
        allTickets.append(dic)
        # 购买成功之后,显示用户所买的彩票(调用显示一张彩票的函数)
        showTicket(dic)
        # 余额递减
        balance -= 2
        # 显示余额
        showBalance()
    else:
        print('余额不足,请及时充值')

# 显示一张彩票
def showTicket(dic):
    # dic = {'red': [31, 4, 7, 24, 10, 30], 'blue': 3}
    # 取红球列表
    red = dic['red']
    # 把红球的数字变为字符串类型
    for i in range(len(red)):
        red[i] = str(red[i])
    # 转化为中间逗号隔开的字符串
    redResult = ','.join(red)
    # 取蓝球
    blue = dic['blue']
    print('红球:',redResult,'蓝球:',blue)

# 显示所有的彩票
def showAllTickets():
    # 每张彩票都在allTickets里面
    for ticket in allTickets:
        # ticket: 字典(每张彩票)
        showTicket(ticket)

# 中奖
def prize():
    global balance
    # 中奖的彩票(随机生成)
    zhongjiang = randomTicket()
    print('中奖的彩票号码为:')
    # 显示一张彩票
    showTicket(zhongjiang)
    # 中奖操作(每个彩票都得判断是否中奖,中的是什么奖)
    for me in allTickets:
        # me: 每一张彩票
        # 自己买的红球
        red = me['red']
        # 自己买的蓝球
        blue = me['blue']
        # 红球的中奖个数
        redCount = 0
        for i in red:
            if i in zhongjiang['red']:
                redCount += 1
        # 蓝球的中奖个数
        blueCount = 0
        if blue == zhongjiang['blue']:
            blueCount += 1
        print(me,redCount, blueCount)
        # 中奖说明
        if redCount == 6 and blueCount == 1:
            print('中6+1')
            # 把1000万加给余额
            balance += 10000000
        elif redCount == 6 and blueCount == 0:
            print('中6+0')
            balance += 5000000
        elif redCount == 5 and blueCount == 1:
            print('中5+1')
            balance += 3000
        elif redCount == 5 and blueCount == 0:
            print('中5+0')
            balance += 200
        elif redCount == 4 and blueCount == 1:
            print('中4+1')
            balance += 200
        elif redCount == 4 and blueCount == 0:
            print('中4+0')
            balance += 10
        elif redCount == 3 and blueCount == 1:
            print('中3+1')
            balance += 10
        elif redCount == 2 and blueCount == 1:
            print('中2+1')
            balance += 5
        elif redCount == 1 and blueCount == 1:
            print('中1+1')
            balance += 5
        elif redCount == 0 and blueCount == 1:
            print('中0+1')
            balance += 5
        else:
            print('很抱歉,该彩票未中奖')

    # 显示余额
    showBalance()


# 主体代码
while True:
    userInput = input('请输入操作序号: ')
    if userInput == '1':
        # 先显示当前余额
        showBalance()
        # 充值
        money = int(input('请输入充值的金额: '))
        addMoney(money)
    elif userInput == '2':
        for i in range(16):
            # 随机购买一张彩票
            randomBuyTicket()
    elif userInput == '3':
        pass
    elif userInput == '4':
        # 中奖
        prize()
    elif userInput == '5':
        # 显示当前余额
        showBalance()
    elif userInput == '6':
        # 显示所有的彩票
        showAllTickets()
    elif userInput == '7':
        # 退出
        print('退出')
        break
    else:
        print('请输入正确的序号')
