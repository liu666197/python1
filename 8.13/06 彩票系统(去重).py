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
balance = 0
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
        # 判断现在生成的彩票是否已经存在在列表当中,如果存在,不能加入到列表当中
        for ticket in allTickets:
            redCount,blueCount = ticketCount(ticket,dic)
            if redCount == 6 and blueCount == 1:
                print('该彩票重复了!!')
                # 执行一遍购买彩票的函数
                # randomBuyTicket()
                # 后面的代码就不用执行了!!!
                return None
        # 把生成的彩票放入allTickets里面
        allTickets.append(dic)
        print('购买成功!!')
        # 购买成功之后,显示用户所买的彩票(调用显示一张彩票的函数)
        showTicket(dic)
        # 余额递减
        balance -= 2
        # 显示余额
        showBalance()
    else:
        print('余额不足,请及时充值')

# 手动输入彩票号码
def inputTicketNum():
    global balance
    while True:
        # 用户的输入内容
        userInput = input('输入彩票号码(总共输入7个号码,每个号码中间逗号隔开,前六个是红球号码,最后一个是蓝球号码): ')
        # 如果用户习惯输入空格
        userInput = userInput.replace(' ', '')
        # 输入的号码多于7或者小于7
        # 根据逗号分割为列表
        userInput = userInput.split(',')
        if len(userInput) == 7:
            # 输入01,02,03
            # ['01','aa','31','020','1','6','8']
            for i in range(len(userInput)):
                # 第一位如果是0,去掉0
                if userInput[i][0] == '0':
                    userInput[i] = userInput[i][1:]
                try:
                    # 将列表中每个元素转化为数字类型 (字母或者数字是会出错的)
                    userInput[i] = int(userInput[i])
                except:
                    # 字母或者汉字
                    print('输入的内容有误,不能出现字母或者汉字或者其他符号!!!')
                    # 输入有误,循环没有必要进行下去
                    break
            # 当循环结束以后,userInput里面就是纯数字类型的列表
            # [1,23,31,020,2,6,1]
            # 红球重复
            # 红球列表
            redList = userInput[:6]
            # 判断红球是否出问题
            flag = False
            for red in redList:
                # red: 每个红球
                # 判断每个红球出现的次数,如果大于1,则重复
                if redList.count(red) > 1:
                    flag = True
                    print('红球当中有重复的数字,请重新输入..')
                    break
                # 判断红球的范围: 1-33
                if red < 1 or red > 33:
                    flag = True
                    print('红球的数字超出范围,应该在1-33之间,请重新输入')
                    break
            if flag:
                # 当红球出现问题,底下的代码不能执行了
                continue
            # 蓝球(最后一项)
            blue = userInput[len(userInput) - 1]
            # 蓝球的范围 1 16
            if blue < 1 or blue > 16:
                print('蓝球的数字超出范围,应该在1-16之间,请重新输入')
            else:
                # 蓝球和红球都没有问题
                # 正常的一张彩票
                dic = {'red': redList, 'blue': blue}
                # 判断现在生成的彩票是否已经存在在列表当中,如果存在,不能加入到列表当中
                for ticket in allTickets:
                    print(ticket,dic)
                    redCount, blueCount = ticketCount(ticket, dic)
                    print(redCount,blueCount)
                    if redCount == 6 and blueCount == 1:
                        print('该彩票重复了!!')
                        # 执行一遍购买彩票的函数
                        # randomBuyTicket()
                        # 后面的代码就不用执行了!!!
                        return None
                # 把生成的彩票放入allTickets里面
                allTickets.append(dic)
                print('购买成功!!')
                # 购买成功之后,显示用户所买的彩票(调用显示一张彩票的函数)
                showTicket(dic)
                # 余额递减
                balance -= 2
                # 显示余额
                showBalance()
                break

        else:
            print('请输入7个号码!!!')

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
        # 直接用每个彩票和中奖的彩票进行比较
        redCount,blueCount = ticketCount(zhongjiang,me)
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

# zhongjiang: 要进行对比的彩票
# me: 自己的彩票或者新生成的彩票
# 两个彩票进行对比
def ticketCount(zhongjiang,me):
    # 前面生成了的彩票
    # zhongjiang = {'red': [20, 22, 14, 18, 12, 8], 'blue': 16}

    # 现在生成的彩票 (现在生成的彩票是否和前面生成过的彩票重合,如果重合,则不能加入到allTickets里面)
    # me = {'red': [21, 20, 25, 14, 18, 4], 'blue': 16}
    # 自己买的红球
    red = me['red']
    # 自己买的蓝球
    blue = me['blue']
    # 红球的中奖个数
    redCount = 0
    for i in red:
        if str(i) in zhongjiang['red']:
            redCount += 1
    # 蓝球的中奖个数
    blueCount = 0
    if blue == zhongjiang['blue']:
        blueCount += 1
    # 返回红球相同的数字和蓝球相同的数字
    return [redCount,blueCount]


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
        for i in range(3):
            # 随机购买一张彩票
            randomBuyTicket()
    elif userInput == '3':
        # 手动输入彩票号码
        inputTicketNum()
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
