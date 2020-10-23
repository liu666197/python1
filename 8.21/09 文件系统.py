
# 模式: r w a
#
# r+: r是主模式,但是写入内容的时候也不会报错 (默认光标在第一个位置)
# with open('1.html','r+',encoding='utf-8') as file:
#     file.write('123')
# w+: w是主模式,读取的时候也不会报错
# with open('1.html','w+',encoding='utf-8') as file:
#     print(file.read())
# a+: a是主模式,光标在文件的末尾
# with open('1.html','a+',encoding='utf-8') as file:
#     print(file.read())
# rb: 二进制的结果
# with open('1.html','rb') as file:
#     print(file.read())
# wb: 写入二进制数据
# with open('1.html','wb') as file:
#     #编码
#     a = '111文字'.encode()
#     file.write(a)
# with open('1.html','rb') as file:
#     print(file.read().decode())
with open('images/aaa/1.html','r',encoding='utf-8') as file:
    print(file.read())