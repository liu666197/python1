# 追加内容: 修改文件内容
file = open('1.txt','a',encoding='utf-8')
print(file.writable())
file.write('aaaa')
file.write('bbbb')
file.writelines(['12312','wqeeqwewq','qwewqewq'])
# 关闭文件
file.close()