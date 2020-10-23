# 创建人的类 (把相同的属性和方法都放在该类当中)
class Person:
    def __init__(self,name,sex,age,height):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
    def eat(self):
        print('%s吃饭了.....'%(self.name))
    def sleep(self):
        print('%s睡觉...'%(self.name))


# 创建学生类的时候,让学生类继承人的类
class Student(Person):
    def __init__(self,name,sex,age,height,score):
        # super(): 父类对象
        # 先调用父类对象的__init__方法
        super().__init__(name,sex,age,height)
        # 再添加自己的新的属性
        self.score = score
    # eat方法重写
    def eat(self):
        print('%s吃红烧肉了.....' % (self.name))
    def test(self):
        print('%s考试'%(self.name))
class Worker(Person):
    # 重写init方法,形参也得写
    def __init__(self,name,sex,age,height,salary):
        # 先调用父类的init方法
        super().__init__(name,sex,age,height)
        # 再给当前对象添加属性
        self.salary = salary
class Doctor(Person):
    def __init__(self,name,sex,age,height,is_zhuzhi):
        super().__init__(name,sex,age,height)
        self.is_zhuzhi = is_zhuzhi

s = Student(name='张三',sex='男',age=18,height=180,score=90)
s.eat()
s.sleep()
print(s.score)
w = Worker(name='李四',sex='男',age=18,height=180,salary=1000)
w.eat()
w.sleep()
# w.test()
d = Doctor(name='王五',sex='男',age=18,height=180,is_zhuzhi=True)
d.eat()
d.sleep()
print(d.is_zhuzhi)