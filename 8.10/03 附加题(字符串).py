# 10.已知字符串 a = “aAsmr3idd4bgs7Dlsf9eAF”,要求如下
a = 'aAsmr3idd4bgs7Dlsf9eAF'
# 	- 请将a字符串的大写改为小写，小写改为大写。
# print(a.swapcase())
# 	- 请将a字符串的数字取出，并输出成一个新的字符串。
# result = ''
# for i in a:
#     # 判断是否为数字
#     if i.isdecimal():
#         result += i
# print(result)
# 	- 请去除a字符串多次出现的字母，仅留最先出现的一个。例 ‘abcabb’，经过去除后，输出 ‘abc’
# result = ''
# # 去重
# for i in a:
#     if i not in result:
#         result += i
# print(result)

# 	- 请将a字符串反转并输出。例：’abc’的反转是’cba’
# a = 'aAsmr3idd4bgs7Dlsf9eAF'
#
# # 将字符串转列表
# b = list(a)
# b.reverse()
# # 把列表转化为字符串
# result = ''.join(b)
# print(result)
# for i in range(len(a) - 1,-1,-1):
#     print(a[i],end='')
# 	- 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）(难)
# 	- 请判断 ‘boy’里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
# 	- 输出a字符串出现频率最高的字母
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# a = list(a) # 将a转换为列表，方便操作
# 使用冒泡排序，比较每个字符的(经过加工的)ASCII码
# "加工"ASCII码：先假定每个字符都是小写，再加上判断其是否真的为小写的布尔值
# 因为布尔值经过隐式转换后为1或0，对整体值的影响较大，因此为提高字符ASCII码对整体值的影响，*2
# for i in range(len(a)-1):
#     flag = False
#     for j in range(len(a)-1):
#         if (ord(a[j].lower())*2 + a[j].islower()) > (ord(a[j+1].lower())*2 + a[j+1].islower()):
#             a[j], a[j+1] = a[j+1], a[j]
#             flag = True
#     if flag == False:
#         break
# print(a)

# 	- 请判断 ‘boy’里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输出False.
# a = 'aAsmr3idd4bgs7Dlsf9eAF'
# b = 'boy'
# flag = True
# for i in b:
#     if i not in a:
#         flag = False
#         # 如果有不在的,结果就是False,后面的不用遍历了
#         break
# print(flag)

# - 输出a字符串出现频率最高的字母 (频率最高的字母有多个)
a = 'aaaAsmr3idd4bgs7Dlsf9eAF'
# 最高频率
max = 0
# 频率最高
for i in a:
    # 如果每个出现的频率大于max,max的值就替换
    if a.count(i) > max:
        max = a.count(i)
result = []
# 如果字母出现的频率要和最大值相等,则就是我们需要的字母
for i in a:
    if a.count(i) == max and i not in result:
        result.append(i)
print(result)