score = [68, 87, 92, 100,100, 76,100,100, 88,100, 54, 89, 76, 61,234,56,67,100,2342,100,213,100]
# 1.查询score列表中成绩是满分的所有的学生学号 index(元素,start,stop)
# count = -1
# # 出现次数
# a = score.count(100)
# b = []
# for i in range(a):
#     count = score.index(100, count + 1)
#     b.append(count)
# print(b)


# # 第一次找出来的
# count = score.index(100,count + 1)
# # 第二次找出来
# count = score.index(100,count + 1)
# # 第三次找出来
# count = score.index(100,count + 1)
# print(count)
# 2.删除score列表中所有的数值100
# # 出现次数
# a = score.count(100)
# for i in range(a):
#     score.remove(100)
# print(score)

# 3.有一个字符串,凡是出现"|"和 " "和 "-"和"," 前后,就算一个单词. 计算下列字符串  str = "hello world,a|nd python or and ddd and hello hello world and python or and dd-dddd and,hello wo|rld and python or and ddd and wor-ld and py-thon or and ddd and an|d ddd and" 单词的个数
# a = "hello world,a|nd python or and ddd and hello hello world and python or and dd-dddd and,hello wo|rld and python or and ddd and wor-ld and py-thon or and ddd and an|d ddd and"
# # 把所有的标点符号替换为空格
# # a = a.replace('|',' ')
# # a = a.replace('-',' ')
# # a = a.replace(',',' ')
# # 链式调用: 对象.方法名().方法名().方法名()
# a = a.replace('|',' ').replace('-',' ').replace(',',' ')
# # 空格出现次数 + 1
# result = a.count(' ') + 1
# print(result)
# 4.编写程序，完成以下要求：
# 	-  统计字符串中，各个字符的个数
# 	-  比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
# a = 'hello world'
# # 列表的方式
# b = []
# # 字符串的方式
# c = ''
# # i: 每个字符
# for i in a:
#     # if i not in b and i != ' ':
#     if i not in c and i != ' ':
#         # b.append(i)
#         # 字符串
#         c += i
#         print(i+':'+str(a.count(i)),end='\t')
a = 'hello world'# 5.给定一个带文件后缀名的字符串,要求: 将后缀名输出来 例如: aasd.sad.sas.da?sdasdsaa.txt  --> txt
# https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
# 先从右往左找.号的位置
# a = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
# # 按照.分割
# b = a.split('.')
# # 取得最后一位
# print(b[len(b) - 1])
# index = a.rfind('.')
# result = ''
# # 从下标位置开始遍历
# for i in range(index + 1,len(a)):
#     result += a[i]
# print(result)

#6.用户输入一堆字符串,打印出最后一个单词的长度 asdsa adasd asdsadas asdsadeasd asdsad
# a = 'asdsa adasd asdsadas asdsadeasd asdsad'
# # 如果有其他符号 先替换为空格
# # 按照空格分割
# b = a.split()
# print(len(b[len(b) - 1]))

# 7.用for循环打印一个菱形. 用center()做 不能是偶数n
# n = 21
# for i in range(1,n + 1,2):
#     a = '*' * i
#     print(a.center(n))
#
# for i in range(n - 2,0,-2):
#     a = '*' * i
#     print(a.center(n))

# 8.要求用户输入字符串,计算一个字符串中所有英文字母的个数.'dsaas12312asSADFSAdas12312dsadsadsadasAASD'
# a = 'dsaas12312asSADFSAdas12312dsadsadsadasAASD'
# ord() : 将字母转化为ascii
# print(ord('A')) # 65
# print(ord('Z')) # 90
# print(ord('a'))  # 97
# print(ord('z'))  # 122
# 把所有的都变为小写
# a = a.lower()
# print(a)
count = 0
# 表示的是数字
# print(a.isdecimal())
# a = 'aaaa'
# print(a.isalpha())
# for i in a:
    # if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
    #     count += 1
    # if i.islower():
    #     count += 1
# a = 'dsaas12312asSADFSAdas12312dsadsadsadasAASD'
# for i in a:
#     if i.isalpha():
#         count += 1
# print(count)

# 9.模拟游戏聊天框,用户能一直输入内容,按回车,打印出用户输入的内容,但是,如果输入的内容当中,有敏感词汇,替换为 *
# 敏感词汇为:  ['sb','SB','sB','Sb','苍老师','你大爷','尼玛','马化腾']
#
# 示例:
# 用户输入的内容为: 你是sb吗?你大爷的,做个人吧
#
# 打印的内容为: 你是**吗?***的,做个人吧
# 敏感词汇
a = ['sb','SB','sB','Sb','苍老师','你大爷','尼玛','马化腾']
while True:
    # 用户输入内容
    # userInput = '你是sb吗?你大爷的,做个人吧'
    userInput = input('请输入聊天内容: ')
    # 判断每一个敏感词汇是否在用户输入的内容当中,如果存在,则替换
    for i in a:
        if i in userInput:
            userInput = userInput.replace(i, '*' * len(i))
    print(userInput)
