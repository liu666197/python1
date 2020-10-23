import re
userInput = input('请输入一个手机号: ')
# 规则
pattern = r'^1[34578]\d{9}$'
pattern = r'1[34578]\d{9}'

result = re.search(pattern,userInput)
# 没有匹配到,None,匹配到,值不为None
if result == None:
    print('不是手机号')
else:
    print('正确的手机号')