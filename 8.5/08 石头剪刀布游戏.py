import random
flag = True
while True:
    # 用户输入0,1,2
    userInput = int(input('用户输入石头(0)  剪刀(1)  布(2): '))
    # 电脑随机生成
    computerInput = random.randint(0, 2)
    # 先按照用户输入的内容和电脑随机生成的内容,获得到底出的是什么
    if userInput == 0:
        user = '石头'
    elif userInput == 1:
        user = '剪刀'
    else:
        user = '布'
    # 电脑
    if computerInput == 0:
        computer = '石头'
    elif computerInput == 1:
        computer = '剪刀'
    else:
        computer = '布'

    # 用户的输入 - 电脑生成的数字 -1,2 就说明是用户胜
    result = userInput - computerInput
    if result == - 1 or result == 2:
        print('用户胜,用户出的为%s,电脑出的为%s' % (user, computer))
        # exit()
        # 让循环终止
        # flag = False
        break
    elif result == 0:
        print('平局,用户出的为%s,电脑出的为%s' % (user, computer))
    else:
        print('电脑胜,电脑出的为%s,用户出的为%s' % (computer, user))


print('循环结束')
print('+++')
print('+++')
print('+++')
print('+++')