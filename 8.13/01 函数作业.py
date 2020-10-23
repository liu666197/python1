# 0.写函数,传入一个参数n,返回n的阶乘的结果
# 例如: cal(5)  返回的结果为: 5 * 4 * 3 *  2 * 1
def cal(n):
    chengji = 1
    for i in range(n,0,-1):
        chengji *= i
    return chengji
# print(cal(5))
# 1.写函数,要求传入列表或者元组,取得下标为偶数的值作为新的列表或者元组,返回给调用者
def a(n):
    # n = [123,1234,2,423,423] --> [123,2,423]
    return n[0::2]
# print(a([123,1234,2,423,423,123,12,312]))
# print(a((12,312,321,43,2,432,432)))
# 2.写函数,判断用户传入的对象(字符串,列表,元组)长度是否大于5
def length(n):
    if len(n) > 5:
        return True
    return False
# 3.写函数,检查列表的长度,如果大于5,则将列表的前5项内容返回给调用者
def b(n):
    if len(n) > 5:
        return n[:6]
# [12312,32,4,234234,23,432432,4,23] return [12312,32,4,234234,23]
#
# 4.写函数,要求传入一个字符串,统计每个字符出现的次数,将其制作为字典返回给调用者
def count(n):
    a = ''
    dic = {}
    for i in n:
        if i not in a and i != ' ':
            a += i
            dic[i] = n.count(i)
    return dic

# print(count('wek  wqekj'))
# wekwqekj  {'w': 2,'e': 2,'k': 2..}
#
# 5.写函数,接收三个参数,返回值较大的那个数字
def max(a,b,c):
    rMax = a
    if rMax < b:
        rMax = b
    if rMax < c:
        rMax = c
    return rMax
# 6.写函数,检查传入字典的每一个value的长度,如果大于2,那么仅保留前两个长度的内容,并组合为新字典返回给调用者
# 例如:
# 传入:
# 	dic = {'k1': 'v1v2','k2': [11,22,33,44]}
# dic[key] = value
# 返回:
# 	dic {'k1': 'v1','k2': [11,22]}
def c(dic):
    for key,value in dic.items():
        if len(value) > 2:
            dic[key] = value[:2]
    return dic
print(c({'k1': 'v','k2': [11,22,33,44]}))