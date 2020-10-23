# - 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）(难)
a = 'aAsmr3idd4bgsBB7Dlsf9eAF'
s = ''
for i in a:
    if i.isalpha():
        s += i
result = ''
# chr(): 将数字转化为字母
# 输出所有的大写字母
for i in range(65,91):
    # 所有的大小写字母
    # chr(i): 大写字母
    # print(chr(i),chr(i + 32))
    upper = chr(i) * s.count(chr(i))
    lower = chr(i + 32) * s.count(chr(i + 32))
    result += upper + lower
print(result)
# # 把a的排序写出来
# # A
# upper = 'A' * a.count('A')
# # a
# lower = 'a' * a.count('a')
# print(upper + lower)
# # 把b的排序写出来
# upper = 'B' * a.count('B')
# lower = 'b' * a.count('b')
# print(upper + lower)
#
# # 把c的排序写出来
# upper = 'C' * a.count('C')
# lower = 'c' * a.count('c')
# print('C:',upper + lower)