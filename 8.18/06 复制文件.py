# 练习: 通过代码的方法,把笔记.txt复制为笔记1.txt!!!
r_file = open('笔记.txt','r',encoding='utf-8')
w_file = open('笔记1.txt','w',encoding='utf-8')

# w_file.write(r_file.read())
# w_file.writelines(r_file.readlines())
for i in r_file:
    # i:每行内容
    w_file.write(i)
# 关闭文件
r_file.close()
w_file.close()