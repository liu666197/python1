a = []
for i in range(1,4):
    print('请输入第%s个人的信息:'%(i))
    name = input('姓名:')
    sex = input('性别:')
    age = input('年龄:')
    jiguan = input('籍贯:')
    dic = {
        "姓名": name,
        '性别': sex,
        '年龄': age,
        '籍贯': jiguan
    }
    a.append(dic)

# 遍历列表
for person in a:
    print(person['姓名'],end=',')
    print(person['性别'],end=',')
    print(person['年龄'],end=',')
    print(person['籍贯'])