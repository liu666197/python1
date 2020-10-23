a = {
    'name': '小明',
    'age': 13,
    'height': 150,
    'weight': 300,
    'like': '篮球'
}
print(a)
# 根据key删除
# a.pop('like')
# 复制字典
b = a.copy()
# 清空字典
# a.clear()
# 给某个key设置一个默认值: a['aaa'] = 'bbb'
# a.setdefault('aaa','bbb')
# a['aaa'] = 'ccc'
# 默认删除最后一项(键值对)
# a.popitem()
# 类似于extend
# 可以将新字典当中的键值对,直接加入到原字典里面
# a.update({'aaa': '111','bbb': '222','ccc': '333'})
# 根据key获取value值:和a[key]类似
a = {
    'name': '小明',
    'age': 13,
    'height': 150,
    'weight': 300,
    'like': '篮球'
}

a['aaa'] = 'ccc'
# get(key,value): 如果key,value不存在,value为None;如果value值存在,key不存在,获取到的值则是value值(默认值),如果字典当中有key,则显示字典中的key所对应的value值
b = a.get('aaa','bbb')
# b = a['aaa']
print(b)
# print(b)