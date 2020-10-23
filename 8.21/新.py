import pymysql
# 数据库连接
db=pymysql.connect('localhost','root','python')
# 生成数据库游标，操作sql函数
cursor=db.cursor()
# 最好要双引号，防止引号
sql = "INSERT INTO people (name,sex,age,height) VALUES ('小红','女',20,170);"
cursor.execute(sql)
db.commit()
db.close()