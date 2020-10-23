import os

# 判断文件夹是否存在
# print(os.path.exists('aaa'))

# 创建文件夹
# os.mkdir('aaa')

if not os.path.exists('aaa'):
    # 创建文件夹
    os.mkdir('aaa')