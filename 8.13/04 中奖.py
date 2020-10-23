# 中奖的彩票
zhongjiang = {'red': [20,22,14,18,12,8],'blue': 16}

# 自己的彩票
me = {'red': [21,20,25,14,18,4],'blue': 16}
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

print(redCount,blueCount)

# 如果是全部都中了,redCount: 6 blueCount: 1

# 彩票重复了? redCount: 6,blueCount: 1