a = {
    'name': '小明',
    'age': 13,
    'height': 150,
    'weight': 300,
    'like': '篮球'
}
# 键值对的个数
print(len(a))
# 遍历的是所有的key
# for i in a:
#     print(i,a[i])

# 遍历每一个键值对
for i in a.items():
    # i[0]: key i[1]:value
    print(i[0],i[1])

# print(a.keys())
# 遍历每一个key
for i in a.keys():
    print(i,a[i])

# 遍历每一个value
for i in a.values():
    print(i)