# 导包
import pymysql

# 创建连接
conn = pymysql.connect(host="localhost",#192.163.0.113
                       port=3306,
                       user="root",
                       password="root123456",
                       database="jcd_test")


cursor = conn.cursor()# 获取游标

sql='select * from students'

cursor.execute(sql)# 执行sql
# result = cursor.fetchall()#获取所有结果
result = cursor.fetchone()#获取第一个结果
print(result)# 打印结果


cursor.close()# 关闭游标
conn.close()# 关闭连接