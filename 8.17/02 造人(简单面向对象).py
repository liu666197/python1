# 对象由类创建
# 创建类
# 创建人
class Person:
    pass

# 创建对象(实例化对象)
p = Person()
# 设置属性
p.name = '张三'
p.sex = '男'
p.height = 180
# 获取属性
print(p.name,p.sex,p.height)
# 创建对象(实例化对象)
p1 = Person()
p1.name = '李四'
p1.sex = '女'
p1.height = 160
print(p1.name,p1.sex,p1.height)