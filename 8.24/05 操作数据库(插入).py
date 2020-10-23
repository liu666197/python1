import pymysql
# 1.连接数据库

# db: database
db = pymysql.connect('localhost','root','','python')
# 生成数据库的游标对象: 操作数据库
cursor = db.cursor()
# sql(最好是双引号,防止符号冲突)
sql = "INSERT INTO people (name,sex,age,height) VALUES ('小红','女',20,170);"
# 执行sql
cursor.execute(sql)

# 如果不想再对数据库进行操作,提交操作(后面不再进行操作)
db.commit()
# 关闭数据库
db.close()