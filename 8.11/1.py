#   12345
dic = {
	'-': 'fu',
	'0': 'ling',
	'1': 'yi',
	'2': 'er',
	'3': 'san',
	'4': 'si',
	'5': 'wu',
	'6': 'liu',
	'7': 'qi',
	'8': 'ba',
	'9': 'jiu',
	'.': 'dian'
}
# 用户输入: 123
shuru = input('请输入一个数: ')
# 末尾是:0    发音: 原来的结果里面截取字符串到十的位置
# 末尾是: 00  发音: 原来的结果里面截取字符串到百的位置
# 末尾是: 000  发音: 原来的结果里面截取字符串到千的位置
# 知道末尾几个0以后,判断这几个0的长度,这个长度作为fayin列表的下标,就能取到对应的十百千万这些数值了
# shuru = input('请输入一个数: ')
fayin =  ['','十','百','千','万','十万','百万']

# # 点号后面的内容
right_result = ''
# # 判断.是否在字符串当中
if '.' in shuru:
    # 根据.把字符串进行分割
    a = shuru.split('.')
    # 左边的内容
    shuru = a[0]
    # 点号的范围 .123
    dian_str = '.' + a[1]
    for i in dian_str:
        right_result += dic[i] + ' '
    # print(right_result)
# 结果
left_result = ''
# 判断是否有负号
if '-' in shuru:
    left_result += 'fu '
    #截取后面的正数部分
    shuru = shuru[1:]
flag = True
for i in range(len(shuru)):
    index = len(shuru) - 1 - i
    if shuru[i] == '0':
        if flag:
            left_result += dic[shuru[i]] + ' '
            flag = False
    else:
        left_result += dic[shuru[i]] + ' ' + fayin[index] + ' '
        flag = True
# 倒过来 (代表末尾有几个0)
shuru = shuru[-1::-1]
count = ''
# 倒着遍历
for i in shuru:
    if i == '0':
        count += i
    else:# 有不连续的0,就不用拼接到count里面去了
        break
# 末尾是:0    发音: 原来的结果里面截取字符串到十的位置
# 末尾是: 00  发音: 原来的结果里面截取字符串到百的位置
# 末尾是: 000  发音: 原来的结果里面截取字符串到千的位置
# 知道末尾几个0以后,判断这几个0的长度,这个长度作为fayin列表的下标,就能取到对应的十百千万这些数值了
# shuru = input('请输入一个数: ')
# fayin =  ['','十','百','千','万']
if count:
    fayin_str = fayin[len(count)]
    # 找出千的位置
    index = left_result.rfind(fayin_str)
    left_result = left_result[0:index + 2]
    # print(left_result[0:index + 1])

# 结果:
result = left_result + right_result
print(result)