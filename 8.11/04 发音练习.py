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
userInput = '111'
result = ''
# i : 每个数字
for i in range(len(userInput)):
    # 当下标为0的时候,怎么让它指向3  4 - 1 - 0
    # 当下标为1的时候,怎么让它指向2 4 - 1 - 1
    # 当下标为2的时候,怎么让它指向1 4 - 1 - 2
    # 发音的下标
    index = len(userInput) - 1 - i
    # print(userInput[i],fayin[index])
    # print(dic[userInput[i]],fayin[index])
    result += dic[userInput[i]] + ' ' + fayin[index] + ' '
print(result)