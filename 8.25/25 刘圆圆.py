# 1.实现一个单例
# class Singleton:
#     instance=None
#     def __new__(cls, *args, **kwargs):
#         if cls.instance==None:
#             cls.instance=super().__new__(cls, *args, **kwargs)
#         return cls.instance
#
# a=Singleton()
# b=Singleton()
# print(id(a),id(b))


# 2.实现冒泡,选择排序
# a = [111,3,45,7,78796,5342,32,367]
# for i in range(len(a)-1):
#     flag=False
#     for j in range(len(a)-1-i):
#         if a[j]>a[j + 1]:
#             flag=True
#             a[j], a[j + 1] = a[j + 1], a[j]
#     if flag==False:
#         break
# print(a)
#选择排序
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)


# 3.输出1-100间的所有质数
# for i in range(2,100):
#     for j in range(2,i):
#         if i % j==0:
#             break
#     else:
#          print(i)


# 4.逗号隔开输入某年某月某日，判断这一天是这一年的第几天？
# # 例如: 输入: 2004,3,1 输出: 61
# # 	  输入: 2005,3,1 输出: 60
# # 1,3,5,7,8,10,12月分别是21天
# # 平年二月28天,闰年二月29天
# year=int(input('请输入年'))
# month=int(input('请输入月'))
# day=int(input('请输入日'))
# # 按照平年来计算,平年和闰年只相差一天
# list={31,60,91,121,152,182,213,244,274,305,335,365}
# # 如果是一月,则日为这是该年的第几天
# if month==1:
#     count=day
# #     判断平年以及闰年
# else:
#     if (year%4==0 and year%100!=0) or year%400==0:
#       if month>1 and month<13:
#         count =list[month-2]+day
#     elif month==2:
#         count=31+day
#     else:
#         count = list[month - 2] + day
# print('第'+str(count)+'天')

# 5.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# 反弹的总高度
# zongHeight=[]
# # 每次反弹高度
# height=[]
# # 起始高度
# start=100
# # 第十次落地
# times=10
# for i in range(2,times+1):
#     if i==2:
#         zongHeight.append(start)
#     else:
#         zongHeight.append(start*2)
#     start/=2
#     height.append(start)
# print('第十次落地共经过高度:zongHeight={0}'.format(sum(zongHeight)))
# print ('第十次反弹高度:height={0}'.format(height[-1]))


#
# 6.将字符串"a-b-c-d-e-f"倒叙输出,中间字符变为大写: “f-e-d-C-b-a”
#  b=a[::-# a=-d-e-f'1]
# c=b.replace('c','C')
# print(c)'a-b-c
#

# 7.实现函数strip,要求自己实现去除字符串首尾空格的功能
# 输入: ‘hello     ’  输出: ‘hello’
# 输入: ‘h   ello     ’  输出: ‘h   ello’
# 输入: ‘   hello     ’  输出: ‘ hello’
# b=str.strip(' ')
# print(b)


# 8.功能描述：删除字符串中字符个数最少的字符，而且最少字符串有多个，最少的要全部删除 然后返回该字符串
# 输入：asdasdasbb
# 输出：asasas
# a='asdasdas'
# min=len(a)
# for i in a:
#     if a.count(i)<min:
#         min=a.count(i)
#
# for i in a:
#     if a.count(i)==min:
#         b=a.replace(i,'')
# print(b)


# 9.随机生成，100个从1到10的随机整数，然后每个偶数出现的次数:
# 例如: 1,2,3,2,3,1,5,6,10,2
# 输出: {“2”: 3,”6”: 1 “10”: 1}
# import random
# dict={}
# for i in range(0,100):
#     n=random.randint(1,10)
#     if n in dict.keys():
#         dict[n]+=1
#     else:
#         dict[n]=1
#     # print (dict.items())
# for i,j in dict.items():
#      print('出现',i,'的次数为:',j,'次')


# 10.用户输入日期,判断是否为日期,格式如下: 2018-12-6,年份1-9999,月份01-12或者1-12,天数01-31或者1-31,不用考虑每个月的具体天数,例如: 2018-2-31也满足
# import re
# a=input('请输入日期（格式如下: 2018-12-6）：')
# pattern=r'^([1-9][0-9]{3})\-([0]?[1-9]|[1][012])\-([0]?[1-9]|[1][1-9]|[2][1-9]|[3][01])$'
# result=re.search(pattern,a)
# print(result)
