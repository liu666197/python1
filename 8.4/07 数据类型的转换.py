# 本身的类型不会发生变化
# a = '20'
# a = '哈哈哈'
a = '10.22'
# 字符串(数字的字符串) --> 数字

# print(int(a),type(int(a)))
# print(float(a),type(float(a)))
# print(a,type(a))
# a = 10.22
# print(int(a))
# a = 10
# print(float(a))
# 其他类型-->字符串
# a = True
# b = 20
# c = str(a) + str(b)
# print(c,type(c))
# 其他类型 --> 布尔(True,False)
# 为false的状态
# a = 0
# a = ''
# a = None
# print(bool(a))
# 做加法计算,用户输入两个数,最后的结果是这两个数的和
# a = int(input('请输入第一个数: '))
# b = int(input('请输入第二个数: '))
# result = a + b
# print(result,type(a),type(b))

a = int(input('请输入一个三位数: '))
# 思路: 将每一位数字取出来,相加即可
# 百位
bai = a // 100
# 十位
shi = a // 10 % 10
# 个位
ge = a % 10
# 结果
result = bai ** 3 + shi ** 3 + ge ** 3
print(result)