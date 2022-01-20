# 导包
import pymysql
# 初始化
conn = None
cursor = None
# 业务处理
try:
    # 创建连接
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="root123456", database="jcd_test", autocommit=False)
    # 获取游标
    cursor = conn.cursor()
    # 执行sql
    # sql = "insert into students(studentNo, name, age) values(48, '西游记', 33);"
    sql = "select * from students;"

    cursor.execute(sql)
    print(cursor.rowcount)
    print("-" * 200)
    # 主动抛出异常
    # raise Exception("程序出错啦。。。。。。")
    # 4).新增一条英雄人物数据（name:孙悟空 gender:1 book_id:4）
    sql = "insert into students(studentNo, name, age) values(46, '黑熊精', 33)"
    cursor.execute(sql)
    print(cursor.rowcount)
    # 提交事务
    conn.commit()
except Exception as e:
    # 回滚数据
    conn.rollback()
    # 打印异常信息
    print(e)
finally:
# 关闭游标
    if cursor: cursor.close()
    # 关闭连接
    if conn:
        conn.close()