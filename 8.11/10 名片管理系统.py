import random
# 提示文字
msg = '''==================================================
   名片管理系统 V0.01
 1. 添加一个新的名片
 2. 删除一个名片 (先查找,是否删除)
 3. 修改一个名片 (先查找,是否修改)
 4. 查询一个名片 
 5. 显示所有的名片 (50条) [{},{},{}]
 6. 退出系统
=================================================='''
print(msg)

# 姓
xing = ["赵","钱","孙","李","周","吴","郑","王","冯","陈","褚","卫","蒋","沈","韩","杨","朱","秦","尤","许","何","吕","施","张","孔","曹","严","华","金","魏","陶","姜","戚","谢","邹","喻","柏","水","窦","章","云","苏","潘","奚","范","彭","郎","鲁","韦","昌","马","苗","凤","花","方","俞","任","袁","柳","酆","鲍","史","唐","费","廉","岑","薛","雷","贺","倪","汤"]
# 名
ming = ["涵清","星舞","秋枫","晨月","霁华","烟霏","殷云","烟岚","霏微","夕佳","思邈","紫琪","雅君","涵","鸿月","茜","雅洁","语彤","梓璇","靖怡","倾哥","清浅","疏影","茗月","醉烟","月墨","云落","桂燕","子琴", "腊梅", "芬", "莉娅", "娟娣", "艳红", "棠莉" ,"悦驰" ,"婉婷", "嘉洁" ,"彩红", "媛雪", "美芳", "束芳", "淑琳", "若瑶","莉轩", "燕齐", "昕妍", "思思" ,"玉瑶" ,"子婧" ,"爱琴", "维娟", "思娜", "欢欢" ,"鸾瑶" ,"玲丽", "旦娅", "苏娟" ,"宝琳" ,"思念","羽洁", "秋艳", "建颖" ,"泓茹", "富霞", "倩成" ,"诗茹" ,"欣瑶", "曦秀", "婷丽", "莉娜" ,"东玲" ,"巧娜" ,"佳艳" ,"蓓莉" ,"纪颖"]
# 地址
addrs = ["北京", "上海", "广州", "深圳", "辽宁", "天津", "四川", "广西", "山东", "山西", "西安", "云南", "新疆", "呼和浩特", "包头", "赤峰", "鄂尔多斯","呼伦贝尔", "阿拉善盟", "济南", "青岛", "烟台", "威海", "潍坊", "德州", "滨州", "东营", "聊城", "菏泽", "临沂", "北京", "上海", "天津", "重庆","淄博", "泰安", "枣庄", "日照", "莱芜", "海阳", "平度", "莱阳", "石家庄", "沧州", "承德", "秦皇岛", "唐山", "保定", "廊坊", "邢台", "衡水"]
# 所有的名片 [{},{},{}]
allData = []
# 生成50条数据
for i in range(50):
    # 姓名
    name = random.choice(xing) + random.choice(ming)
    # qq
    qq = random.randint(1000000000,9999999999)
    # 微信
    wechat = random.randint(10000000000,99999999999)
    # 地址
    addr = random.choice(addrs)
    dic = {'姓名': name,'qq': qq,'微信': wechat,'地址': addr}
    allData.append(dic)
print(len(allData))

# 一个名片  {'姓名': xxx,'qq': xxxxx,'微信': xxxxx,'地址': xxxxc}


while True:
    userInput = input('请输入操作序号: ')
    if userInput == '1':
        # 添加名片
        name = input('请输入要添加的姓名:')
        qq = input('请输入要添加的qq:')
        wechat = input('请输入要添加的微信:')
        addr = input('请输入要添加的地址:')
        # 输入的数据拼凑成一个字典
        dic = {'姓名': name, 'qq': qq, '微信': wechat, '地址': addr}
        # 加入到总的数据里面
        allData.append(dic)
        print('添加成功!!!')
    if userInput == '2':
        # 删除
        name = input('请输入要删除的姓名: ')
        # 先查找该名字是否存在
        flag = True
        # 使用while循环进行删除,不会造成下标的移动
        i = 0
        while i < len(allData):
            person = allData[i]
            if name in person['姓名']:
                flag = False
                for data in person.values():
                    print(data, end='\t')
                # 是否删除
                isDelete = input('是否删除?y/n')
                if isDelete in 'yY是':
                    # 直接删除
                    allData.remove(person)
                    # 下标得-1
                    i -= 1
                print()
            i += 1
        # 如果flag的值还是True,说明没有找到该人
        if flag:
            print('你要删除的人不存在')
    if userInput == '3':
        # 修改
        name = input('请输入要修改的姓名: ')
        # 先查找该名字是否存在
        flag = True
        # 使用while循环进行删除,不会造成下标的移动
        i = 0
        while i < len(allData):
            # 把列表中的元素赋值给了person
            person = allData[i]
            if name in person['姓名']:
                flag = False
                for data in person.values():
                    print(data, end='\t')
                print()
                # 是否删除
                isDelete = input('是否修改?y/n')
                if isDelete in 'yY是':
                    # 用户输入 (当用户输入为空的时候,显示原来的内容)
                    updateName = input('姓名: ') or person['姓名']
                    qq = input('qq: ') or person['qq']
                    wechat = input('微信: ') or person['微信']
                    addr = input('地址: ') or person['地址']
                    # 修改
                    allData[i]['姓名'] = updateName
                    allData[i]['qq'] = qq
                    allData[i]['微信'] = wechat
                    allData[i]['地址'] = addr
                    print('修改成功!!!')
            i += 1
        # 如果flag的值还是True,说明没有找到该人
        if flag:
            print('你要修改的人不存在')
    if userInput == '4':
        # 查询
        name = input('请输入要查询的姓名: ')
        flag = True
        for person in allData:
            if name in person['姓名']:
                flag = False
                for data in person.values():
                    print(data, end='\t')
                print()
        # 如果flag的值还是True,说明没有找到该人
        if flag:
            print('查无此人')
    if userInput == '5':
        # 显示所有
        for person in allData:
            # person: 每一张名片
            for data in person.values():
                print(data,end='\t')
            print()
            # print(person)
            # print(person['姓名'],end='\t')
            # print(person['qq'],end='\t')
            # print(person['微信'],end='\t\t')
            # print(person['地址'])
    if userInput == '6':
        print('退出操作!!!')
        break
