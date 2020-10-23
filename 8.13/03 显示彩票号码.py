dic = {'red': [31, 4, 7, 24, 10, 30], 'blue': 3}
red = dic['red']

# 常用做法
redResult = ''
for i in red:
    redResult += str(i) + ','
redResult = redResult[:len(redResult) - 1]
blue = dic['blue']
# print('红球:',red,'蓝球: ',blue)
print('红球: ',redResult,'蓝球:',blue)

# join方法
a = [31, 4, 7, 24, 10, 30]
for i in range(len(a)):
    a[i] = str(a[i])
print(a)
# 转字符串,中间逗号隔开
result = ','.join(a)
print(result)