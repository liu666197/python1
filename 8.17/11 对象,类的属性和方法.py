class Person:
    # 类的属性
    count = 0
    a = 10
    b = 20
    def __init__(self):
        # 实例属性
        self.name = 'zs'
        self.age = 10
        # 私有属性
        self.__aa = 20
    # 实例方法
    def eat(self):
        print('吃饭了',self.__aa)
        # 访问私有方法
        self.__sleep()
    # 私有方法
    def __sleep(self):
        print('睡觉了')
    # 类方法
    @classmethod
    def test(cls):
        # cls: 类名
        print(Person.count,cls.count)

# 获取类属性
print(Person.a)
p = Person()
# print(p.__aa)
print(p.name)
p.eat()
# p.__sleep()
# 调用类方法
print(Person.test())