a = 10
# 将a的值赋值给b
b = a
# 将20赋值给b
b = 20
print(a,b)

print(id(a))

a = [10,20,30]
b = a
b[0] = 50
a[1] = 100
print(a[0],b[0])
print(a,b)

a = []
dic = {}
for i in range(1,4):
    print('请输入第%s个人的信息:'%(i))
    name = input('姓名:')
    sex = input('性别:')
    age = input('年龄:')
    jiguan = input('籍贯:')

    dic['姓名'] = name
    dic['性别'] = sex
    dic['年龄'] = age
    dic['籍贯'] = jiguan
    a.append(dic)

print(a)