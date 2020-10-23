# 6.模拟英雄联盟中的游戏人物的类:
# 	要求:
# 		a.创建Role(角色)类,有name,ad(攻击力),hp(血量)三个属性
# 		b.创建Arms(武器)类,有name,ad(攻击力),两个属性
# 		c.创建一个attack方法,此方法是实例化的两个对象,互相用武器攻击的功能
# 			例:
# 				实例化一个Role对象,名字为盖伦,ad为10,hp为100
# 				实例化另一Role个对象,名字为亚索,ad为20,hp为80
# 				实例化一个Arms对象,名字为无尽之刃,ad为40
#
# 		  attack方法要完成: '谁拿什么武器攻击谁,谁掉了多少血,还剩多少血的提示功能'
class Role:
    def __init__(self,name,ad,hp):
        self.name = name
        self.ad = ad
        self.hp = hp
    def attack(self,a,b):
        # a: 被攻击的角色
        # b: 武器对象
        # 掉血: 本身的攻击力 + 武器的攻击力
        a.hp -= (self.ad + b.ad)
        print('%s拿%s攻击%s,%s掉了%s血,还剩%s血...'%(self.name,b.name,a.name,a.name,self.ad + b.ad,a.hp))
        # 剩余血量
        # a.hp -= self.ad
        # print('{}攻击了{},{}掉了{}的血,还剩下{}血!!'.format(self.name,a.name,a.name,self.ad,a.hp))
class Arms:
    def __init__(self,name,ad):
        self.name = name
        self.ad = ad
gailun = Role('盖伦',10,100)
yasuo = Role('亚索',20,80)
wuqi = Arms('无尽之刃',40)
gailun.attack(yasuo,wuqi)
