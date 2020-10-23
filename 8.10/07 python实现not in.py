#
a = [12,343,54365,467,57]
result = 3431
# 判断一个数在不在列表 (not in)
flag = False
for i in a:
    if i == result:
        flag = True
        break
print(flag)