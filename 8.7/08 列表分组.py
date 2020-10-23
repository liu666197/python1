# 4.请写出一段 Python 代码实现分组一个 list 里面的元素, [1,2,3,...100]变成 [[1,2,3], [4,5,6]....,[97,98,99],[100]]
# a.假设列表的元素有200个呢?那你的代码还能有效吗?
# b.假设列表里面的元素不是有序的?那你的代码还能生效吗?任意的列表

allList = list(range(1,102))
# print(allList)
# allList = [231,345,6,7,132,342,67,8,234,65,11,213,324]
# 结果: [[231,345,6],[7,132,342],[67,8,234],[65]]
result = []
for i in range(len(allList)):
    # 3个一组
    if i % 3 == 0:
        a = []
        # print(i)
        a.append(allList[i])
        # 确保不会超出列表的下标范围
        if i + 1 < len(allList):
            # print(i + 1)
            a.append(allList[i + 1])
        if i + 2 < len(allList):
            a.append(allList[i + 2])
        # 把每个分组的列表添加到总列表当中
        result.append(a)
print(result)

# # 先做第一项
# a = []
# a.append(allList[0])
# a.append(allList[1])
# a.append(allList[2])
# result.append(a)
# # 先做第二项
# a = []
# a.append(allList[3])
# a.append(allList[4])
# a.append(allList[5])
# result.append(a)
# print(a,result)

