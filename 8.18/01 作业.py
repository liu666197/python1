# 1.Employee 类
# 	- 员工数 初始值为0, 每当新声明一个实例时,员工数加一
# 	- 员工: 姓名, 工资
# 	- 声明方法 displayCount: 打印出当前的总员工数 (类方法)
# 	- displaySalary : 打印每一个员工自己的名字和薪水.
class Employee:
    # 类属性
    count = 0
    def __init__(self,name,salary):
        # 让员工数加1就行
        Employee.count += 1
        self.name = name
        # 私有属性
        self.__salary = salary
    # 实例方法
    def displaySalary(self):
        print('{}的工资是{}'.format(self.name,self.__salary))
    # 类方法
    @classmethod
    def displayCount(cls):
        # cls: 类名
        print('当前员工总数为: {}'.format(cls.count))

# 实例化
e = Employee('张三1',10000)
e = Employee('张三2',10000)
e.displaySalary()
#类方法的调用
Employee.displayCount()

# 2.设计一个人的类,有名字,体重;能吃,能跑;
# 	a.每次跑步会减肥0.5公斤
# 	b.每次吃东西体重会增加1公斤
# 	c.有个get_msg()方法,打印出名字,体重:
# 		我的名字叫: xxx 体重是:
class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def eat(self):
        self.weight += 1
        print('能吃')
    def run(self):
        self.weight -= 0.5
        print('能跑')
    def get_msg(self):
        print('我的名字叫: %s 体重是:%s'%(self.name,self.weight))
import math
print(math.pow(2,3))
print(math.pi)
# 3.定义一个圆类,有半径属性,其中有计算周长和面积的方法
class Circle:
    def __init__(self,r):
        self.r = r
    # 周长
    def zhouchang(self):
        # print('周长: %s'%(2 * math.pi * self.r))
        print('周长: %.2f'%(2 * math.pi * self.r))
    # 面积
    def mianji(self):
        print('面积: %s'%(math.pi * self.r ** 2))

# 4.补充代码实现:
# 	user_list = []
# 	while True:
# 		user_name = input('输入用户名: ')
# 		sex = input('输入性别: ')
# 		age = input('输入年龄: ')
# 		email = input('输入邮箱: ')
# 	a.把每个用户用对象表示
# 	b.当列表中添加3个对象以后,打印出3个对象的信息:
# 		我叫xxx,性别xx,今年xx岁了,我的邮箱是xxxx
class Person:
    def __init__(self,name,age,sex,email):
        self.name = name
        self.age = age
        self.sex = sex
        self.email = email

# user_list = []
# for i in range(3):
#     user_name = input('输入用户名: ')
#     sex = input('输入性别: ')
#     age = input('输入年龄: ')
#     email = input('输入邮箱: ')
#     p = Person(user_name,age,sex,email)
#     user_list.append(p)
# for i in user_list:
#     print('我叫{},性别{},今年{}岁了,我的邮箱是{}'.format(i.name,i.sex,i.age,i.email))

# 对象的引用
p1 = Person('张三',20,'女','123@163.com')
p2 = Person('张三',20,'女','123@163.com')
print(p1,p2)
# a = p
# a.name = '李四'
# print(a.name, p.name)