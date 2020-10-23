# a = True
# b = False
# # 隐式转换: a-->1 b --> 0
# c = a + b
# print(c,type(c))
# or: 只要一个条件成立,整体就成立
# and: 所有条件成立,整体才成立
# a = 0 or 20
# 如果数值都是True的数值,取最后一个数值;如果有为False(0,'')的数值,取第一个为False的数值
a = 0 and 20

print(a)