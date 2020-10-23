# 5.模拟英雄联盟中的游戏人物的类:
#  要求:
#   a.创建Role(角色)类
#   b.初始化方法中给对象封装 name,ad(攻击力),hp(血量)三个属性
#   c.创建一个attack方法,此方法是实例化的两个对象,互相攻击的功能
#    例:
#     实例化一个Role对象,盖伦,ad为10,hp为100
#     实例化另一个Role对象,亚索,ad为20,hp为80
#     attack方法要完成: '谁攻击谁,谁掉了多少血,还剩多少血的提示功能'
class Role:
    def __init__(self,name,ad,hp):
        self.name = name
        self.ad = ad
        self.hp = hp
    def attack(self,a):
        # 剩余血量
        a.hp -= self.ad
        print('{}攻击了{},{}掉了{}的血,还剩下{}血!!'.format(self.name,a.name,a.name,self.ad,a.hp))
gailun = Role('盖伦',10,100)
yasuo = Role('亚索',20,80)
# 盖伦调用attack方法: 由盖伦攻击其他对象
gailun.attack(yasuo)
gailun.attack(yasuo)
gailun.attack(yasuo)
gailun.attack(yasuo)
yasuo.attack(gailun)