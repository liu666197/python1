# 1.调用列表操作的常用函数实现以下功能:
# 	- 1)创建一个空列表score
score = []
# 	- 2)在score列表中依次追加10个数值([68, 87, 92, 100, 76, 88, 54, 89, 76, 61] )
# 		extend(列表)
score.extend([68, 87, 92, 100, 76, 88, 54,88,88 ,89, 88, 59, 59, 76, 61,59])
#  		append(能放任意数据类型)
# 	- 3)输出score列表中第3个元素的数值 score[2]
# 	- 4)输出score列表中第1～6个元素的值
# for i in range(0,6):
#     print(score[i])
# for i in range(6):
#     print(score[i])
# 	- 5)在score列表第3个元素之前添加数值59
score.insert(2,59)
# 	- 6)利用变量num保存数值76，查询76分在score列表中出现的次数
# num = 76
# print(score.count(num))
# 	- 7)查询列表中是否有num76分的考试成绩
# print(76 in score)
# print(score.index(76))
# 	- 8)查询score列表中成绩是满分的学生学号
# print(score.index(100))
# 	- 9)score列表中将59分加1分 (如果有多个59)
# score[2] += 1
# 先判断59出现了几次
# result = score.count(59)
# for i in range(result):
#     # 查找59出现的位置
#     index = score.index(59)
#     print(index)
#     score[index] += 1

# print(score)
# 	- 10)删除score列表中第1个元素
# score.pop(0)
# 	- 11)获得score列表中元素的个数
# print(len(score))
# 	- 12)对列表中所有元素进行排序，输出考试的最高分和最低
# score.sort()
# print('最高分为: %s,最低分为: %s'%(score[len(score) - 1],score[0]))
# 	- 13)颠倒score列表中元素的顺序
# score.reverse()
# 	- 14)删除score列表中尾部的元素
# score.pop(len(score) - 1)
# score.pop()
# 	- 15)score列表中追加数值88，并输出。删除score列表中所有的88
# score.append(88)
# result = score.count(88)
# for i in range(result):
#     score.remove(88)
# 	- 16)创建2个列表score1和score2,score1中包含数值2个元素值80,61,score2中包含3个元素值71,95,82，合并这两个列表，并输出全部元素
# score1 = [80,61]
# score2 = [71,95,82]
# score1.extend(score2)
# print(score1)
# print(score1 + score2)

# 	- 17)创建score1列表，其中包含数值2个元素值80,61，将score1中元素复制5遍保存在score2列表中，输出score2列表中全部元素。
# score1 = [80,61]
# score2 = []
# for i in range(5):
#     score2.extend(score1)
# print(score2)
# a = '*' * 5
# print(a)
# score1 = [80,61]
# score2 = score1 * 5
# print(score2)
# 2.[68, 87, 92, 100, 76, 88, 54, 89, 76, 61] 去除列表中的偶数  --> [87,89,61]
a = [68, 87, 92, 100, 76, 88, 54,33,76,87,91]
# 下标: 0   1   2    3    4    5  6
#      87  100  76  88  54
#

# print(a)
# for i in a:
#     if i % 2 == 0:
#         a.remove(i)
# print(a)
# b = []
# for i in a:
#    # 如果不是偶数,那么就加入到b列表当中
#     if i % 2 != 0:
#         b.append(i)
# print(b)
# 如果需要在遍历列表的过程中删除列表里面的元素,使用while循环,在删除以后,将下标的值减1即可
a = [68, 88, 92, 100, 76, 88, 54,33,76,87,91]
# 下标: 0   1   2    3    4    5  6
#      88  92  100  76  88  54
#  原理: 当删除元素的时候,元素的下标会往前移一位,但是遍历下标的次数还是依次进行
print(a)
i = 0
while i < len(a):
    if a[i] % 2 == 0:
        a.remove(a[i])
        # 让下标值-1
        i -= 1
    i += 1
print(a)