import re
a = '12321jhj213123jlk23lk43j23jkl43l2jk4jkl32'
# 只匹配到第一个内容就结束了
# result = re.search('\d+',a)
# 查找出所有符号规则的内容
# 匹配所有的数字
# result = re.findall('\d+',a)
result = re.findall('[a-z]+',a)
print(result)