# coding: utf-8
############### 2020/08//10 作业 - 10 阎杉杉 ###############
# 0.任意选取豆瓣电影top250的5条数据用数据类型表示出来 (字典和列表的组合 列表包5个字典)
# movieList = []
# dict1 = {'name': {'中文名': '肖申克的救赎',
#                   '英文名': 'The Shawshank Redemption',
#                   '港译名': '月黑高飞(港)',
#                   '台译名': '刺激1995(台)'},
#          'play': '[可播放]',
#          'director': {
#                     '中文名': '弗兰克·德拉邦特',
#                     '英文名': 'Frank Darabont'},
#          'lead1': {'中文名': '蒂姆·罗宾斯',
#                     '英文名': 'Tim Robbins'},
#          'year': 1994,
#          'country': '美国',
#          'type': ['犯罪', '剧情'],
#          'rating': 9.7,
#          'population': 1956099,
#          'intro': '希望让人自由。'
#          }
# dict2 = {'name': {'中文名': '霸王别姬',
#                   '英文名': 'Farewell My Concubine'},
#          'play': '[可播放]',
#          'director': {
#                     '中文名': '陈凯歌',
#                     '英文名': 'Kaige Chen'},
#          'lead1': {'中文名': '张国荣',
#                     '英文名': 'Leslie Cheung'},
#          'lead2': {'中文名': '张丰毅',
#                     '英文名': 'Fengyi Zhang'},
#          'year': 1993,
#          'country': '中国大陆 中国香港',
#          'type': ['剧情', '爱情', '同性'],
#          'rating': 9.6,
#          'population': 1444228,
#          'intro': '风华绝代。'
# }
# dict3 = {'name': {'中文名': '阿甘正传',
#                   '英文名': 'Forrest Gump',
#                   '其它译名': '福雷斯特·冈普'},
#          'play': '[可播放]',
#          'director': {
#                     '中文名': '罗伯特·泽米吉斯',
#                     '英文名': 'Robert Zemeckis'},
#          'lead1': {'中文名': '汤姆·汉克斯',
#                     '英文名': 'Tom Hanks'},
#          'year': 1994,
#          'country': '美国',
#          'type': ['剧情', '爱情'],
#          'rating': 9.5,
#          'population': 1484955,
#          'intro': '一部美国近现代史。'
# }
# dict4 = {'name': {'中文名': '这个杀手不太冷',
#                   '英文名': 'Léon',
#                   '其它译名': '杀手莱昂',
#                   '台译名': '终极追杀令'},
#          'director': {
#                     '中文名': '吕克·贝松',
#                     '英文名': 'Luc Besson'},
#          'lead1': {'中文名': '让·雷诺',
#                     '英文名': 'Jean Reno'},
#          'lead2': {'中文名': '娜塔莉·波特曼',
#                     '英文名': '...'},
#          'year': 1994,
#          'country': '法国',
#          'type': ['剧情', '动作', '犯罪'],
#          'rating': 9.4,
#          'population': 1679349,
#          'intro': '怪蜀黍和小萝莉不得不说的故事。'
# }
# dict5 = {'name': {'中文名': '美丽人生',
#                   '意文名': 'La vita è bella',
#                   '港译名': '一个快乐的传说(港)',
#                   '英文名': 'Life Is Beautiful'
#                   },
#          'director': {
#                     '中文名': '罗伯托·贝尼尼',
#                     '英文名': 'Roberto Benigni'},
#          'lead1': {'中文名': '罗伯托·贝尼尼',
#                     '英文名': 'Roberto Beni'},
#          'year': 1997,
#          'country': '意大利',
#          'type': ['剧情', '喜剧', '爱情', '战争'],
#          'rating': 9.5,
#          'population': 937934,
#          'intro': '最美的谎言。'
# }
# movieList.append(dict1)
# movieList.append(dict2)
# movieList.append(dict3)
# movieList.append(dict4)
# movieList.append(dict5)
# print(movieList)

# 1.有字符串"key1:1|key2:2|key3:3|key4:5"处理成字典{'key1':1,'key2': 2...}
# a = "key1:1|key2:2|key3:3|key4:5"
# dictA = {}
# for i in a.split("|"):
#     dictA[i.split(":")[0]] = int(i.split(":")[1])
# print(dictA)

# 2.有列表a，将所有大于60的值保存在字典的第一个key中,将小于60的值保存在第二个key中:
# 格式: {'key1': 大于60的值列表,'key2': 小于60的值列表}
# a = [11,77,22,33,88,44,55,77,88,70,30,99]
# dictA = {'key1': [],'key2': []}
# li1 = []
# li2 = []
# for i in a:
#     if i >= 60:
#         li1.append(i)
#     else:
#         li2.append(i)
# dictA['key1'] = li1
# dictA['key2'] = li2
# print(dictA)

# 3.输出商品列表, 用户输入序号, 显示用户选中的商品
# 商品列表:
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799], ['wife', 10], ['wifi', 100000]]

# a.把商品列表变为:
# productsNew = []
# for i in products:
#     dict = {'name': '', 'price': ''}
#     dict['name'] = i[0]
#     dict['price'] = i[1]
#     productsNew.append(dict)
# products = productsNew
# print(products)

# b.在a的基础上, 页面显示: 序号 + 商品名称 + 商品价格:
# for i in range(0, len(products)):
#     print(i+1)
#     print(products[i]['name'])
#     print(products[i]['price'])

# c.用户输入商品的序号, 打印商品名称和价格
# num = input('请输入商品序号：')
# num = int(num)
# print("商品名称：%s，价格：%s" % (products[num-1]['name'], products[num-1]['price']))

# d.如果用户输入的商品序号有误(没有该商品), 提示输入有误, 并重新输入
# num = input('请输入商品序号：')
# num = int(num)
# if num >= 1 and num <= len(products):
#     print("商品名称：%s，价格：%s" % (products[num-1]['name'], products[num-1]['price']))
# else:
#     print("商品序号有误")

# e.用户输入Q或者q, 退出程序
# num = input('请输入商品序号：')
# if num.lower() == 'q':
#     exit()
# num = int(num)
# if num >= 1 and num <= len(products):
#     print("商品名称：%s，价格：%s" % (products[num-1]['name'], products[num-1]['price']))
# else:
#     print("商品序号有误")

# 4.电影投票,由用户给每个电影打分,最终显示每个电影的评分(用户输入分数);
# 电影列表:
# list = ['囧妈','疯狂的外星人','金瓶梅','战狼','哪吒传奇','灵魂摆渡']
#
# ratingDict = {}
# for i in list:
#     rating = input("请给%s打分: " % (i))
#     ratingDict[i] = int(rating)
# print(ratingDict)

# 5.车牌区域计数:
# 所有的车牌号:
# cars = ['京A88888','赣B12345','沪C76543','黑B33445','京B22445','沪A67854','黑C67890']
# locals = {'沪': '上海','黑': '黑龙江','赣': '江西','京': '北京'}

# 以下代码运行结果为：{'上海': 2, '黑龙江': 2, '江西': 1, '北京': 2}
# 与所给的结果{'黑龙江': 2,'上海': 2,'北京': 2,'江西': 1}顺序不符
# stats = {} #建立一个储存结果的字典
# for i in locals.items():
#     count = 0
#     for car in cars:
#         if i[0] == car[0]:
#             count += 1
#             stats[i[1]] = count
# print(stats)

# 6.
# zhubo = {'卢本伟': 5000000,'冯提莫': 8888,'UZI': 8000000000,'mlxg': 1000000,'letme': 88888888,'张琪格': 1000,'陈一发': 50000}
# # 	a.计算主播的平均收益
# sum = 0
# for income in zhubo.values():
#     sum += income
# average = sum/len(zhubo)
# print(average)
#
# # 	b.删除利益小于平均值的主播
# zhuboNew = {}
# for i in zhubo.items():
#     if i[1] < average:
#         zhuboNew[i[0]] = i[1]
# print(zhuboNew)

# 7.根据以下字典,把数字的发音读出来
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
# userInput = input("请输入一个数: ")
# print("发音为：", end="")
# for i in userInput:
#     for pronunce in dic.items():
#         if i == pronunce[0]:
#             print(pronunce[1], end=" ")

# 8. 只需做三位数和四位数的
userInput = input("请输入一个数: ")
# 先建立一个储存第7题格式读音的列表
output = []
for i in userInput:
    for pronunce in dic.items():
        if i == pronunce[0]:
            output.append(pronunce[1])
# 确定数字长度
if userInput[0].isdecimal():
    length = len(userInput)
else:
    length = len(userInput) - 1
# 输出读音
if length == 4:
    output.insert(-1, "十")
    output.insert(-3, "百")
    output.insert(-5, "千")
if length == 3:
    output.insert(-1, "十")
    output.insert(-3, "百")
output = ' '.join(output)
print(output)

# 9. 将以下字符串变为字典的格式:
# link = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=json"
# # 将字符串转为列表，根据"="和"&"分割单词
# link = link.replace("?", " ").replace("=", " ").replace("&", " ")
# linkLi = link.split(" ")
# linkLi.pop(0) # 去除前面的https://www.baidu.com/s
# # 建立输出字典
# linkDic = {}
# for i in range(len(linkLi)):
#     if i%2 == 0:
#         linkDic[linkLi[i]] = linkLi[i+1]
# print(linkDic)

# 10. 名片管理系统 (不考虑重复)
# surnameLi = ["赵","钱","孙","李","周","吴","郑","王","冯","陈","褚","卫","蒋","沈","韩","杨","朱","秦","尤","许","何","吕","施","张","孔","曹","严","华","金","魏","陶","姜","戚","谢","邹","喻","柏","水","窦","章","云","苏","潘","奚","范","彭","郎","鲁","韦","昌","马","苗","凤","花","方","俞","任","袁","柳","酆","鲍","史","唐","费","廉","岑","薛","雷","贺","倪","汤"]
# givennameLi = ["涵清","星舞","秋枫","晨月","霁华","烟霏","殷云","烟岚","霏微","夕佳","思邈","紫琪","雅君","涵","鸿月","茜","雅洁","语彤","梓璇","靖怡","倾哥","清浅","疏影","茗月","醉烟","月墨","云落","桂燕","子琴", "腊梅", "芬", "莉娅", "娟娣", "艳红", "棠莉" ,"悦驰" ,"婉婷", "嘉洁" ,"彩红", "媛雪", "美芳", "束芳", "淑琳", "若瑶","莉轩", "燕齐", "昕妍", "思思" ,"玉瑶" ,"子婧" ,"爱琴", "维娟", "思娜", "欢欢" ,"鸾瑶" ,"玲丽", "旦娅", "苏娟" ,"宝琳" ,"思念","羽洁", "秋艳", "建颖" ,"泓茹", "富霞", "倩成" ,"诗茹" ,"欣瑶", "曦秀", "婷丽", "莉娜" ,"东玲" ,"巧娜" ,"佳艳" ,"蓓莉" ,"纪颖"]
# locationLi = ["北京", "上海", "广州", "深圳", "辽宁", "天津", "四川", "广西", "山东", "山西", "西安", "云南", "新疆", "呼和浩特", "包头", "赤峰", "鄂尔多斯","呼伦贝尔", "阿拉善盟", "济南", "青岛", "烟台", "威海", "潍坊", "德州", "滨州", "东营", "聊城", "菏泽", "临沂", "北京", "上海", "天津", "重庆","淄博", "泰安", "枣庄", "日照", "莱芜", "海阳", "平度", "莱阳", "石家庄", "沧州", "承德", "秦皇岛", "唐山", "保定", "廊坊", "邢台", "衡水"]
#
# import random
# flag = True
# while flag == True:
#     # 首先，随机生成50条数据
#     li = []
#     for i in range(51):
#         name = random.choice(surnameLi) + random.choice(givennameLi)
#         qq = random.randint(1000000000, 9999999999)
#         wechat = random.randint(10000000000, 99999999990)
#         add = random.randint(0, 9) #没看明白题目，住址是随机数字？
#         dic = {'姓名': name, 'QQ号': qq, '微信号': wechat, '住址': add}
#         li.append(dic)
#
#     # 询问用户想要进行什么操作
#     operation = input("请问您要进行什么操作（增 删 改 查 显示所有，q退出）？")
#
#     # 1）添加一个新的名片，同以上循环中的代码【增】
#     if operation == "增":
#         nameInput = input("请输入名字：")
#         qqInput = input("请输入qq：")
#         wechatInput = input("请输入微信：")
#         addInput = input("请输入住址：")
#         new = {'姓名': nameInput, 'QQ号': qqInput, '微信号': wechatInput, '住址': addInput}
#         li.append(new)
#
#     # 2）删除一个名片(先查找, 是否删除)【删】
#     if operation == "删":
#         userInput = "请输入要删除的名字："
#         nameList = []
#         for i in li:
#             nameList.append(i.get('姓名'))
#         if userInput not in nameList:
#             print("该姓名不存在")
#         else:
#             confirm = input("确认删除有关%s的记录吗（是/否）？" % (userInput))
#             if confirm == "是":
#                 li.pop(nameList.index(userInput))
#
#     # 3）修改一个名片(先查找, 是否修改)
#     if operation == "改":
#         userInput = input("请输入要修改的名字：")
#         nameList = []
#         for i in li:
#             nameList.append(i.get('姓名'))
#         if userInput not in nameList:
#             print("该姓名不存在")
#         else:
#             nameInput = input("请输入名字：")
#             qqInput = input("请输入qq：")
#             wechatInput = input("请输入微信：")
#             addInput = input("请输入住址：")
#             # 要更改的记录index为：
#             adjustIndex = nameList.index(userInput)
#             # 更改内容
#             li[adjustIndex]['姓名'] = nameInput
#             li[adjustIndex]['QQ号'] = qqInput
#             li[adjustIndex]['微信号'] = wechatInput
#             li[adjustIndex]['住址'] = addInput
#
#     # 4）查询一个名片
#     if operation == "查":
#         userInput = input("请输入要查询的名字：")
#         nameList = []
#         for i in li:
#             nameList.append(i.get('姓名'))
#         if userInput not in nameList:
#             print("该姓名不存在")
#         else:
#             print(li[nameList.index(userInput)])
#
#     # 5）显示所有的名片(50条) [{}, {}, {}]
#     if operation == "显示所有":
#         print(li)
#
#     # 6）退出系统
#     if operation.lower() == "q":
#         flag = False
