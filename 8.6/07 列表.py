a = [213,34,67,987,908]
print('修改前:',a)
# 增
# 在列表的末尾追加元素 (只能放一个参数)
# a.append(10)
# a.append(20)
# a.append('aaa')
# a.append(30)
# a.append([1,2,3])
# 只能放一个参数,只能是列表
# iterable: 列表 (可迭代,可遍历)
# 扩展列表 (适合一次性添加多个数据)
# a.extend([1,2,3])
# 在哪个下标的位置插入元素
# a.insert(0,10)

# 删
# 根据元素值删除
# a.remove(213)
# 清空列表
# a.clear()
# 根据下标删除元素
# a.pop(1)

# 改 (通过下标的方式修改)
# a[0] = 30
# print('修改后:',a)
# a = [213,34,67,987,908,213,213]

# 查: 查找出来的内容最好拿个变量去接收一下
# 元素的出现次数
# result = a.count(213)
# 查找第一个元素出现的位置
# result = a.index(213)
# print(result)

# 其他方法
# 拷贝列表
# b = a.copy()
# print(a)
# print(b)
# 翻转列表
# a.reverse()
# 列表排序
# a.sort()
# print('修改后:',a)

# 判断一个数据在不在一个列表里面
print(213 in a)
print(213 not in a)
a = []
for i in range(1,101):
    a.append(i)
print(a)