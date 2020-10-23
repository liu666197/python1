# 单例: 无论生成几个对象,这几个对象都是指同一个对象
# 每次实例化对象的时候,只开辟一片空间
class Singleton:
    # 类属性
    instance = None
    # 构造函数: 开辟一片对象的内存空间
    def __new__(cls, *args, **kwargs):
        # cls: 类名
        if cls.instance == None:
            cls.instance = super().__new__(cls,*args,**kwargs)
        # 得执行父类里面的new方法,才能开辟空间
        return cls.instance
    def __init__(self):
        print(222)
        pass

# 实例化对象
p1 = Singleton()
p2 = Singleton()
p3 = Singleton()
print(p1,p2,p3)