import random
# 3.双色球: 红色球可以在1-33个编号中任意选择6个，蓝色球可以在1-16中选择一个
# 要求: 随机生成双色球,使用列表输出,前6个红球,最后1个是篮球 (去重,random)

# 把6个红球拿出来
# all = []
# # 当产生的随机数不在列表当中,加入到列表里面去
# while True:
#     num = random.randint(1,33)
#     if num not in all:
#         all.append(num)
#     if len(all) == 6:
#         break
# blue = random.randint(1,16)
# all.append(blue)
# print(all)
# 5. 用户输入n,生成含有 n 个元素值为 1~n 的列表,元素顺序随机,但值不重复:
# 	8  [1,2,3,4,5,8,6,7]
# 	3  [1,3,2]
# n = int(input('请输入一个数字: '))
# result = []
# while True:
#     num = random.randint(1,n)
#     if num not in result:
#         result.append(num)
#     if len(result) == n:
#         break
# print(result)


# 生成1-n的列表

# a = []
# for i in range(1,n + 1):
#     a.append(i)
n = int(input('请输入一个数字: '))
a = list(range(1,n + 1))
result = random.sample(a,n)
print(result)
