# 创建类
class Person:
    # 初始化方法 (构造函数) 创建对象的时候,默认执行的方法
    def __init__(self,name,sex,height):
        self.name = name
        self.sex = sex
        self.height = height
    # 吃饭
    def eat(self):
        # self: 谁调用该方法,self就是谁
        print('%s吃饭了..'%(self.name))
    # 睡觉
    def sleep(self):
        print('%s正在睡觉'%(self.name))
# 实例化(创建)对象
p = Person('张三','男',180)
# print(p.name,p.sex,p.height)
# 调用方法
p.eat()
p.sleep()
# 创建第二个对象
p1 = Person('李四','女',160)
# print(p1.name,p1.sex,p1.height)
p1.eat()
p1.sleep()