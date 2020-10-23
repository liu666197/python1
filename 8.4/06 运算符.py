# 算术运算符: + - * / % // **
# a = 10
# b = 3
# print(a % b)
# print(b % a)
# 取整(取整数部分)
# print(a // b)
# a的b次方
# print(a ** b)
# +
a = 'hello'
b = 'world'
d = '你好世界'
c = a + ' ' + b + ' ' + d
print(c,type(c))
# - : 左右两边不能是字符串
a = '20'
b = 10
# c = a - b
# print(c)
# * : 复制符号 (左右两边同时不能是字符串)
a = 'a'
b = 5
c = b * a * 2
print(c,type(c))
# 练习: 随便设置任意一个三位数,求这三位数的每位数的和.
a = 456
# 思路: 将每一位数字取出来,相加即可
# 百位
bai = a // 100
# 十位
shi = a // 10 % 10
# 个位
ge = a % 10
# 结果
result = bai + shi + ge
print(result)