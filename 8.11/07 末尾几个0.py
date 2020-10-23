a = '3000'
# 计数
count = 0
# 从后往前遍历,如果有0,则让count+1
a = a[::-1]
print(a)
for i in a:
    if i == '0':
        count += 1
    else:# 0 是不连续
        break
fayin = ['','十','百','千','万']

result = 'san 千 ling'
# 末尾的0的个数 需要的发音
# print(fayin[count])
# 查找发音在原来字符串中的位置
index = result.find(fayin[count])
result = result[0:index + 1]
print(index,result)