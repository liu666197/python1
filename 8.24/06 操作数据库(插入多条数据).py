import pymysql
data = [
    {'姓名': '张三','性别': '男','年龄': 20,'身高': 180},
    {'姓名': '张三','性别': '男','年龄': 18,'身高': 160},
    {'姓名': '王五','性别': '男','年龄': 23,'身高': 150},
    {'姓名': '赵六','性别': '女','年龄': 25,'身高': 190},
    {'姓名': '田七','性别': '男','年龄': 21,'身高': 170}
]
# 1.连接数据库
# db: database
db = pymysql.connect('localhost','root','','python')
# 生成数据库的游标对象: 操作数据库
cursor = db.cursor()

# 插入多条数据
for i in data:
    # sql(最好是双引号,防止符号冲突)
    sql = "INSERT INTO people (name,sex,age,height) VALUES ('%s','%s','%s','%s');"%(i['姓名'],i['性别'],i['年龄'],i['身高'])
    print(sql)
    # 执行sql
    cursor.execute(sql)

# 如果不想再对数据库进行操作,提交操作(后面不再进行操作)
db.commit()
# 关闭数据库
db.close()