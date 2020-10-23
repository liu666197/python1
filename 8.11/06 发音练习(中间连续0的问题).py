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
fayin = ['','十','百','千','万','十万']
# 用户输入内容
userInput = '2000'
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

print(result)
# result: er 万 ling  # 截取到er 万
