# 年满18以后,可以去网吧上网;否则,回家写作业..
# age = int(input('请输入你的年龄: '))

# 多重if
# if age >= 18:
#     print('去网吧上网!!!')
# if age < 18:
#     print('回家写作业')

# if..else结构
# if age >= 18:
#     print('去网吧上网')
# else:
#     print('回家写作业')

# if的嵌套: if语句里面再嵌套if语句
# 结婚,有房,考虑一下,没有房,say goodbye;有房又有车的时候,直接结婚
house = input('请输入是否有房: ')
if house == '是':
    car = input('请输入是否有车:')
    if car == '是':
        print('咱们结婚吧..')
    else:
        print('考虑一下..')
else:
    print('say goodbye')










