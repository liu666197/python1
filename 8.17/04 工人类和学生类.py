# 学生类
class Student:
    def __init__(self,name,sex,age,height,score):
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.score = score
    def eat(self):
        print('%s在吃饭...'%(self.name))
    def sleep(self):
        print('%s在睡觉...'%(self.name))
    def test(self):
        print('%s在考试'%(self.name))

# 工人类
class Worker:
    def __init__(self,name,sex,age,height,salary):
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.salary = salary
    def eat(self):
        print('%s在吃饭...'%(self.name))
    def sleep(self):
        print('%s在睡觉...'%(self.name))
    def work(self):
        print('%s在上班'%(self.name))

# 实例化对象
# s = Student('张三','男','18',180,90)
s = Student(name='张三',sex='男',age=18,height=180,score=90)
s.eat()
s.sleep()
s.test()
# 工人对象
w = Worker(name='张三',sex='男',age=18,height=180,salary=90)
w.eat()
w.sleep()
w.work()