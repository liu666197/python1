# 写文件: 修改文件内容
file = open('1.txt','w',encoding='utf-8')
# 写的方法
# print(file.writable())
# 直接写入内容
# file.write('asdasd')
# file.writelines('奥术大师大多')
# file.writelines(['奥术大师大多','12312312','123'])
# 关闭文件
file.close()