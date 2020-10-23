import json
data = [
    {'姓名': '张三','性别': '男','年龄': 20,'身高': 180},
    {'姓名': '张三','性别': '男','年龄': 18,'身高': 160},
    {'姓名': '王五','性别': '男','年龄': 23,'身高': 150},
    {'姓名': '赵六','性别': '女','年龄': 25,'身高': 190},
    {'姓名': '田七','性别': '男','年龄': 21,'身高': 170},
    {'姓名': '田七','性别': '男','年龄': 21,'身高': 170},
    {'姓名': '田七','性别': '男','年龄': 21,'身高': 170},
    {'姓名': '田七','性别': '男','年龄': 21,'身高': 170},
    {'姓名': '田七','性别': '男','年龄': 21,'身高': 170},
]

dic = {
    'data': data
}
# 写入
with open('2.json','w',encoding='utf-8') as file:
    #将字典转化为json字符串,再写入
    # ensure_ascii: 默认为True(把中文或者字母转化为ascii)
    # indent: 缩进,每行内容都进行缩进(格式化)
    file.write(json.dumps(dic,ensure_ascii=False,indent=4))

    # 直接将字典写入到json文件
    json.dump(dic,file,ensure_ascii=False,indent=4)

# 读取json文件内容
with open('站酷.json','r',encoding='utf-8') as file:
    # 字符串
    content = file.read()
    # 字符串 --> json数据(字典)
    content = json.loads(content)
    # print(type(content),content['data'][0]['姓名'])
    # 直接从文件当中读取json内容
    content = json.load(file)
    # print(type(content), content['data'][0]['姓名'])
    print(content,len(content['data']))