# 7.成绩等级:
# 	90分以上:  等级为A
#
# 	80-90: 等级为B
#
# 	60-80: 等级C
#
# 	0-60: 等级为D
score = int(input('输入成绩: '))
if score >= 90:
    print('A')
elif score >= 80: # score < 90
    print('B')
elif score >= 60: # score < 80
    print('C')
else: # 前面条件都不成立的时候执行的代码
    print('D')

holiday_name = input('输入名称: ')
if holiday_name == '情人节':
    print('买玫瑰／看电影')
elif holiday_name == '平安夜':
    print('买苹果／吃大餐')
elif holiday_name == '生日':
    print('买蛋糕')
else:
    print('每天都是节日')


# if  score >= 90:
#     print('A')
# if score >= 80 and score < 90:
#     print('B')
# if score >= 60 and score < 80:
#     print('C')
# if score >= 0 and score < 60:
#     print('D')