

class Mother:
    def __init__(self):
        print('1111')
        self.beauty = True
    def sleep(self):
        print('睡觉')
    def eat(self):
        print('M吃饭')

class Father:
    def __init__(self):
        print(222)
        self.IQ = 100
    def eat(self):
        print('F吃饭..')

class Son(Mother,Father):
    # def eat(self):
    #     print('+++++++++++')
    # 要继承所有父类的属性,必须通过子类调用父类的init方法.默认情况下,只执行第一个父类的init方法
    def __init__(self):
        # super(): 第一个父类
        # 直接写父类的名字
        Mother.__init__(self)
        Father.__init__(self)
        self.name = 'aaa'
    pass
s = Son()
s.sleep()
s.eat()
print(s.beauty)