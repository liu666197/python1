# 0.任意选取豆瓣电影top250的5条数据用数据类型表示出来 (字典和列表的组合  列表包5个字典)
# data = [
#     {
#         "名字": '肖申克的救赎',
#         '别名': ['The Shawshank Redemption','月黑高飞(港)','刺激1995(台)'],
#         '导演': {'中文名': '弗兰克·德拉邦特','英文名': 'Frank Darabont'},
#         '主演': [{'中文名': '蒂姆·罗宾斯','英文名': 'Tim Robbins'}]
#     },
#     {
#         "名字": '霸王别姬',
#         '别名': ['再见，我的妾','Farewell My Concubine'],
#         '导演': {'中文名': '陈凯歌','英文名': 'Kaige Chen'},
#         '主演': [{'中文名': '张国荣','英文名': 'Leslie Cheung'},{'中文名': '张丰毅','英文名': 'Fengyi Zha'}]
#     }
# ]

# 1.有字符串"key1:1|key2:2|key3:3|key4:4"处理成字典{'key1':1,'key2': 2...}
# 把 | 替换为: ,按照:进行分割,结果为列表
a = 'key11232131:1213213|key1232132:212321321|key1231233:312321|key123213214:412312312'
a = a.replace('|',':')
b = a.split(':')
# print(b)
dic = {}
# 遍历列表,按照下标遍历
for i in range(0,len(b),2):
    print(b[i],b[i + 1])
    dic[b[i]] = b[i + 1]
# print(dic)

# 9.将以下字符串变为字典的格式:
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=json
#
# {"ie":"utf-8","f":"8","rsv_bp":"1","rsv_idx":"1","tn":"baidu","wd":"json}
# a = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=json'
# # 查找?的位置,从位置后面一个地方截取到最后
# index = a.rfind('?')
# a = a[index + 1:]
# # 先将&替换为=
# a = a.replace('&','=')
# b = a.split('=')
# dic = {}
# # 遍历列表,按照下标遍历
# for i in range(0,len(b),2):
#     print(b[i],b[i + 1])
#     dic[b[i]] = b[i + 1]
# print(dic)

# 2.有列表a = [11,77,22,33,88,44,55,77,88,70,30,99],将所有大于60的值保存在字典的第一个key中,将小于60的值保存在第二个key中:
# 格式: {'key1': 大于60的值列表,'key2': 小于60的值列表}
# a = [11,77,22,33,88,44,55,77,88,70,30,99]
# key1 = []
# key2 = []
# for i in a:
#     if i > 60:
#         key1.append(i)
#     else:
#         key2.append(i)
#
# dic = {'key1': key1,'key2': key2}
# print(dic)

# 3.3.输出商品列表,用户输入序号,显示用户选中的商品
# 商品列表:
products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],['wife',10],['wifi',100000]]
# 	a.把商品列表变为:
# 	products = [{'name': 'iphone8','price': 6888},{'name': 'MacPro','price': 14888},{'name': '小米6','price': 2499},{'name': 'Coffe','price': 31}....]
# a = []
# for name,price in products:
#     dic = {'name': name, 'price': price}
#     a.append(dic)
# for i in products:
#     print(i[0],i[1])
#     dic = {'name': i[0],'price': i[1]}
#     a.append(dic)
products = a
# print(products)
# 	b.在a的基础上,页面显示: 序号 + 商品名称 + 商品价格:
#
# 				1  iphone8  6888
# 				2  MacPro   14888
# 				3  小米6    2499
# for i in range(len(products)):
#     print(i + 1,products[i]['name'],products[i]['price'])
# 	c.用户输入商品的序号,打印商品名称和价格
#
# 	d.如果用户输入的商品序号有误(没有该商品),提示输入有误,并重新输入
#
# 	e.用户输入Q或者q,退出程序
# while True:
#     try:
#         userInput = input('请输入商品序号: ')
#         if userInput in 'Qq':
#             print('退出')
#             break
#         elif int(userInput) > 0 and int(userInput) <= len(products):
#             index = int(userInput) - 1
#             print('商品为: {},价格为: {}'.format(products[index]['name'], products[index]['price']))
#         else:
#             print('请输入正确的商品序号')
#     except:
#         print('输入有误!!!!!')

# while True:
#     userInput = input('请输入商品序号: ')
#     if userInput in 'Qq':
#         print('退出')
#         break
#     elif userInput.isdecimal():
#         if int(userInput) > 0 and int(userInput) <= len(products):
#             index = int(userInput) - 1
#             print('商品为: {},价格为: {}'.format(products[index]['name'], products[index]['price']))
#         else:
#             print('请输入正确的商品序号')
#     else:
#         print('输入有误!!!')

# 4.电影投票,由用户给每个电影打分,最终显示每个电影的评分(用户输入分数);
# 电影列表: list = ['囧妈','疯狂的外星人','金瓶梅','战狼','哪吒传奇','灵魂摆渡']
#
# 格式如下:
# 请给囧妈打分: 8
# 请给疯狂的外星人打分: 10
# ...
# ...
#
# 显示的结果:
# {'囧妈': 8,'疯狂的外星人': 10...}
# list = ['囧妈','疯狂的外星人','金瓶梅','战狼','哪吒传奇','灵魂摆渡']
# dic = {}
# for movie in list:
#     score = input('请给%s打分: '%(movie))
#     dic[movie] = score
# print(dic)

# 5.车牌区域计数:
# 所有的车牌号:
cars = ['京A88888','赣B12345','沪C76543','黑B33445','京B22445','沪A67854','黑C67890']
#
locals ={'沪': '上海','黑': '黑龙江','赣': '江西','京': '北京'}
#
# 运行结果为:
# {'黑龙江': 2,'上海': 2,'北京': 2,'江西': 1}
# 最终的结果
# result = {}
# for key,value in locals.items():
#     # 每个地方的计数
#     count = 0
#     for car in cars:
#         if key == car[0]:
#             count += 1
#         # if key in car:
#         #     count += 1
#     result[value] = count
# print(result)
# 6.
# zhubo = {'卢本伟': 5000000,'冯提莫': 8888,'UZI': 8000000000,'mlxg': 1000000,'letme': 88888888,'张琪格': 1000,'陈一发': 50000}
# 	a.计算主播的平均收益
# 	b.删除利益小于平均值的主播
# zhubo = {'卢本伟': 5000000,'冯提莫': 8888000000,'UZI': 8000000000,'mlxg': 1000000,'letme': 88888888,'张琪格': 1000,'陈一发': 50000}
# new_zhubo = zhubo.copy()
# # 总收益
# sum = 0
# for price in zhubo.values():
#     sum += price
# # 平均值
# aver = sum / len(zhubo)
# print(aver)
# # 让每个人的收益和平均值比较,如果小,则删除
# for key,value in zhubo.items():
#     if value < aver:
#         new_zhubo.pop(key)
# zhubo = new_zhubo
# print(zhubo)

#
# 7.根据以下字典,把数字的发音读出来
# 运行:
# 请输入一个数: -328
# 发音为: fu san er ba
dic = {
	'-': 'fu',
	'0': 'ling',
	'1': 'yi',
	'2': 'er',
	'3': 'san',
	'4': 'si',
	'5': 'wu',
	'6': 'liu',
	'7': 'qi',
	'8': 'ba',
	'9': 'jiu',
	'.': 'dian'
}
userInput = input('请输入一个数: ')
result = ''
for i in userInput:
    result += dic[i] + ' '
print(result)