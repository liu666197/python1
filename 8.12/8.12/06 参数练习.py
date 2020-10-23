# 1. [12,12,234,32,32,234] [13,14,123,13,14,234] [1,1,1,1,324,23,4,32,2,2] (实现列表去重操作)
# 去重
def quchong(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b
# 选择排序: 每一位都和后面所有的元素进行比较,如果前面比后面的值大,则交换
def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i + 1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
# print(selectionSort([13,14,123,13,14,234]))

# 冒泡排序: 相邻两位的元素进行比较,如果前面比后面的值大,则交换
def bubbleSort(arr):
    for i in range(len(arr) - 1):
        flag = True
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                flag = False
                arr[j],arr[j + 1] = arr[j + 1],arr[j]
        if flag:
            break
    return arr
print(bubbleSort([13,14,123,13,14,234]))

# 求某个范围的和
def qiuhe(a,b):
    sum = 0
    for i in range(a, b + 1):
        sum += i
    return sum
print(qiuhe(1,100))
print(qiuhe(500,1000))
print(qiuhe(3000,5000))