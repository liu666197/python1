import pymysql
# 1.连接数据库
# hostname: 主机名
# root: 登录用户
# password: 密码
# name: 数据库名
# port: 默认为3306 (mac为: 8889)
# pymysql.connect(hostname,root,password,name)
# windows密码为空 mac的密码: root
# db: database
db = pymysql.connect('localhost','root','','python')
# mac
# pymysql.connect('localhost','root','root')
# 生成数据库的游标对象: 操作数据库
cursor = db.cursor()
# sql(最好是双引号,防止符号冲突)
sql = "select * from people"
# 执行sql
cursor.execute(sql)
# cursor.fetchAll(): 执行的结果
print(cursor.fetchall(),type(cursor.fetchall()))
# 如果不想再对数据库进行操作,提交操作(后面不再进行操作)
db.commit()
# 关闭数据库
db.close()