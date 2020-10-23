import re
# 1.检索邮箱:
# @前面可以有字母数字下划线
# @后面都不能有下划线,可以有数字或者字母
# 21312321@qq.com
# abc@163.com
# hwqeqewyh@aaaedu.cc
# a@sad.com.cc
# abc@wqeq.org
# abc_abc@abc.abc
# a@163.abc

# 拆: 左边@ \w+@
# @右边第一块 [0-9a-z]{2,10}
# .字母(整体) {1,2}

# 拼接: \w+@[0-9a-z]{2,10}(\.[0-9a-z]{2,6}){1,2}
test = 'a@163.abc'
pattern = r'^\w+@[0-9a-z]{2,10}(\.[0-9a-z]{2,6}){1,2}$'
result = re.search(pattern,test,re.I)
if result:
    print('正确的邮箱号')
else:
    print('格式不对')
# 2.检验身份证号:
# 18位:
# 1位不能是0  [1-9]
# 2-17: 纯数字 \d{16}
# 18: 数字或者x [0-9x] \d|x
test = '11111111111111111x'
pattern = r'^[1-9]\d{16}[0-9x]$'
result = re.search(pattern,test,re.I)
if result:
    print('正确号')
else:
    print('格式不对')

# 3.校验网址
# 	http://www.baidu.com
# 	http://baidu.com
# 	www.baidu.com
# 	https://www.baidu.com
# 	tieba.baidu.com
# 	news.baidu.com
# 	yuan.news.baidu.com
# 	news.baidu.com.cn

#  http:// 整体 ?  (https?://)?
# //后面第一块 [0-9a-z]{3,10}

# .字母数字(整体) {1,3}
test = 'news.baidu.com.cn'
pattern = r'^(https?://)?[0-9a-z]{3,10}(\.[a-z0-9]{2,}){1,3}$'
result = re.search(pattern,test,re.I)
if result:
    print('正确网址')
else:
    print('格式不对')

