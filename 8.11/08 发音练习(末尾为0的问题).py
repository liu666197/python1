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
# 构建发音列表
fayin = ['','十','百','千','万']
# 用户输入内容
userInput = '10000'
result = ''
# 查看0的状态
flag = True
# i : 每个数字
for i in range(len(userInput)):
	# 发音的下标
	index = len(userInput) - 1 - i
	if userInput[i] == '0':
		if flag == True:
			result += dic[userInput[i]] + ' '
			flag = False
	else:
		flag = True
		result += dic[userInput[i]] + ' ' + fayin[index] + ' '

# result: er 万 ling  # 截取到er 万
# 末尾有几个0
a = userInput
# print(a)
# 计数
count = 0
# 从后往前遍历,如果有0,则让count+1
a = a[::-1]
for i in a:
	if i == '0':
		count += 1
	else:# 0 是不连续kjh;
		break
# print(result)
if count > 0:
	# 查找发音在原来结果中的位置
	index = result.find(fayin[count])
	result = result[0:index + 1]
print(result)