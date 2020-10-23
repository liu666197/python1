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
userInput = '10001'
result = ''
# i : 每个数字
for i in range(len(userInput)):
	# 发音的下标
	index = len(userInput) - 1 - i
	if userInput[i] == '0':
		result += dic[userInput[i]] + ' '
	else:
		result += dic[userInput[i]] + ' ' + fayin[index] + ' '
print(result)