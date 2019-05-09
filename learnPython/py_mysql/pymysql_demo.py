# -*- encoding: utf-8 -*-

import pymysql
import logging

# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

# filename='test_py_logging.log'
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT) # 'module' object has no attribute 'basicConfig'因为起的文件名是logging








mysql_ip = "localhost"
mysql_user = "root"
mysql_pwd = "*****"
mysql_db = "db1"

# open mysql database
try:
    db = pymysql.connect(mysql_ip, mysql_user, mysql_pwd, mysql_db)
    logging.info("login database: " + mysql_db + " successfully")
except:
    logging.info("failed to login database: " + mysql_db)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


def create_table(table_name):
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS " + table_name)
    # 使用预处理语句创建表
    sql = "CREATE TABLE " +  table_name + "(FIRST_NAME  CHAR(20) NOT NULL, LAST_NAME  CHAR(20), AGE INT,  SEX CHAR(1), INCOME FLOAT )"
    try:
        cursor.execute(sql)
        logging.info("Create the table " + table_name + " successfully.")

    except:
        logging.info("Failed to create table " + table_name)



def insert_table(table_name):
    # SQL 插入语句
    sql = "INSERT INTO " + table_name + " (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Mac', 'Mohan',  20,  'M',  2000)"
    logging.info("execute sql：" + sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

def select_data_table(table_name):
    # SQL 查询语句
    sql = "SELECT * FROM " + table_name + " WHERE INCOME > %s" % str(1000)
    logging.info("execute sql：" + sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果logging.info("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % (fname, lname, age, sex, income))
    except:
        logging.info("Error: unable to fetch data")


def update_table(table_name):
    # SQL 更新语句
    sql = "UPDATE " + table_name + " SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
    logging.info("execute sql：" + sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


def delete_data_table(table_name):
    # SQL 删除语句
    sql = "DELETE FROM " + table_name + " WHERE AGE > %s" % str(20)
    logging.info("execute sql：" + sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


create_table("A1")
insert_table("A1")
select_data_table("A1")

update_table("A1")
select_data_table("A1")

delete_data_table("A1")


# 关闭数据库连接
db.close()
