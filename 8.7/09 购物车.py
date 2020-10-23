# 7.写一个循环，不断的问用户想买什么，用户选择一个商品编号(下标)，就把对应的商品添加到购物车(列表)里，最终用户输入q退出时，打印购物车里的商品列表. 数据
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],['wife',10],['wifi',100000]]
#
# 结果: 输出买的所有商品名字,格式为:
# 	总价为: xx元
# 价格和商品名字一一对应
products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],['wife',10],['wifi',100000]]
# 总价
totalPrice = 0
# 购物车
shoppingCar = []
while True:
    try:
        shuru = input('请输入你要购买的商品序号: ')
        if shuru == 'q':
            print('退出购买!!!')
            break
        elif int(shuru) >= 0 and int(shuru) < len(products):
            # 商品编号(下标)
            num = int(shuru)
            # 购买了商品的价格: 买一个就算一个: products[num][1]
            totalPrice += products[num][1]
            # 提示购买的商品的名字: products[num][0]
            print(products[num][0])
            # 将购买的商品加入到购物车
            shoppingCar.append(products[num][0])
        else:
            print('请输入存在的商品编号!!!')
    except:
        print('请输入正确的编号!!!!')

# 循环结束以后,打印出购买的商品信息
print('总价为: %s'%(totalPrice))
# 购买的商品信息
print(shoppingCar)
# 对购物车里面的商品名字进行去重操作
quchongShoppingCar = []
for name in shoppingCar:
    if name not in quchongShoppingCar:
        quchongShoppingCar.append(name)
# 最终输出结果
print('你购买的商品为:',end='\t')
for name in quchongShoppingCar:
    # 去重以后的名字在原来的列表当中出现的次数
    print('%s: %s'%(name,shoppingCar.count(name)),end='\t')