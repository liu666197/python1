import csv

# 数据
data = [
    {
        "名字": '肖申克的救赎',
        '别名': ['The Shawshank Redemption','月黑高飞(港)','刺激1995(台)'],
        '导演': {'中文名': '弗兰克·德拉邦特','英文名': 'Frank Darabont'},
        '主演': [{'中文名': '蒂姆·罗宾斯','英文名': 'Tim Robbins'}]
    },
    {
        "名字": '霸王别姬',
        '别名': ['再见，我的妾','Farewell My Concubine'],
        '导演': {'中文名': '陈凯歌','英文名': 'Kaige Chen'},
        '主演': [{'中文名': '张国荣','英文名': 'Leslie Cheung'},{'中文名': '张丰毅','英文名': 'Fengyi Zha'}]
    }
]
# 转换(处理)数据: 让用户能看懂数据
for i in data:
    i['别名'] = '/'.join(i['别名'])
    i['导演'] = i['导演']['中文名'] + ' ' + i['导演']['英文名']
    a = [y['中文名'] + ' ' + y['英文名'] for y in i['主演']]
    result = '/'.join(a)
    i['主演'] = result
print(data)
# 表头
header = ['名字','别名','导演','主演']
# 写入文件
with open('豆瓣.csv','w',encoding='utf-8-sig',newline='') as file:
    # 写入者对象
    csv_file = csv.DictWriter(file,header)
    # 写入表头
    csv_file.writeheader()
    # 写入多条数据
    csv_file.writerows(data)