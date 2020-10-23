import re
userInput = input('请输入一个座机号: ')
pattern = r'^(0\d{2,3}-)?\d{7}$'

result = re.search(pattern,userInput)

if result == None:
    print('不是座机号')
else:
    print('是座机号')
