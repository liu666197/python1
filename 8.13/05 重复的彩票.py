

# 如果是全部都中了,redCount: 6 blueCount: 1

# 彩票重复了? redCount: 6,blueCount: 1

# 函数: 比较两个彩票的红球和蓝球的相同数字的个数
# zhongjiang: 要进行对比的彩票
# me: 自己的彩票或者新生成的彩票
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
        if i in zhongjiang['red']:
            redCount += 1
    # 蓝球的中奖个数
    blueCount = 0
    if blue == zhongjiang['blue']:
        blueCount += 1
    # 返回红球相同的数字和蓝球相同的数字
    return [redCount,blueCount]
    # return redCount # 函数到这代码就结束
    # return blueCount


# # 中奖的彩票
# dic1 = {'red': [20, 22, 14, 18, 12, 8], 'blue': 16}
#
# # 自己买的彩票
# dic2 = {'red': [21, 20, 25, 14, 18, 4], 'blue': 16}
# 红球相同个数
# print(ticketCount(dic1,dic2)[0])
# # 蓝球的相同个数
# print(ticketCount(dic1,dic2)[1])
#
# # 解构
# redCount,blueCount = ticketCount(dic1,dic2)
#
# print(redCount,blueCount)

# 前面生成过的彩票
dic1 = {'red': [2,25,20,18,8,10],'blue': 5}
# 现在生成的彩票
dic2 = {'red': [20,18,2,25,8,10],'blue': 5}

redCount,blueCount = ticketCount(dic1,dic2)
if redCount == 6 and blueCount == 1:
    print('两个彩票一样')
    print(redCount,blueCount)












