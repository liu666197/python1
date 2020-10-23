# 读文件
# 打开文件
# 绝对路径
# file = open('C:\\Users\\Master\\Desktop\\笔记.txt','r',encoding='utf-8')
# 相对路径
file = open('01 练习.py','r',encoding='utf-8')
# 读取文件所有内容
# print(file.read(2))
# print(file.read(2))
# 读取文件的两个字节的内容
# print(file.read(2))
# print(file.read())
# print(file.read())
# 是否可以读
# print(file.readable())
# 读取一行
# print(file.readline(),end='+++')
# print(file.readline(),end='+++')
# print(file.readline())
# 读取多行
# print(file.readlines())
# 遍历句柄 (每次只读取一行内容,当读取大文件的时候,不容易发生崩溃)
for i in file:
    # i: 就代表每行内容
    print(i)
    print('+++')

# 关闭文件
file.close()

