# 冒泡排序: 将相邻的两个数进行比较,如果前面的数要大于后面的数,则交换两个元素位置
# 			[234,454,623,43543]
#
# 			     [5,4,3,2,1]
# 最多 n - 1 次
#
# 第一次: i = 0  len(a) - 1- 0	    45321 43521 43251 43215  (相邻两个数的比较操作)  最后一位一定是最大值,下一次整体比较的时候,最后一位就不用比较

# 第二次: i = 1  len(a) - 1 - 1

# 第三次: i = 2  len(a) - 1 - 2

# 常规冒泡写法
# 控制排列的次数: 最多n - 1
a = [23,12,40,60,30,324,3534,5]
# # 循环的总次数: n - 1
# for i in range(len(a) - 1):
#     # 标志: 代表前面两个数是否发生交换
#     flag = False
#     # 相邻两个数的比较
#     for j in range(len(a) - 1 - i):
#         # 当前下标: j
#         # 后一位下标: j + 1
#         # 两个数实现了交换
#         if a[j] > a[j + 1]:
#             a[j],a[j + 1] = a[j + 1],a[j]
#             flag = True
#     # 相邻两个数比较循环的结束后,flag还是为False,说明排序已经完成
#     if flag == False:
#         break
    # print(a)

for i in range(len(a) - 1):
    flag = False
    for j in range(len(a) - 1 - i):
        if a[j] > a[j + 1]:
            flag = True
            a[j],a[j + 1] = a[j + 1],a[j]
    if flag == False:
        break
print(a)