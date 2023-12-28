
import pymysql
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
# 从配置文件中获取数据库连接信息
host = config.get('database', 'host')
user = config.get('database', 'user')
passwd = config.get('database', 'passwd')
port = config.getint('database', 'port')
# 连接到数据库
db = pymysql.connect(host=host, user=user, passwd=passwd, port=port)
# 使用 cursor() 方法创建一个游标对象
cursor = db.cursor()
# 查询所有数据库的名称
cursor.execute("SHOW DATABASES")
# 获取所有数据库的名称
all_databases = cursor.fetchall()
# 打印所有数据库的名称
for database in all_databases:
    print(database[0])
# 如果test数据库不存在，则创建它
# if ('wechatDB',) not in all_databases:
#     cursor.execute("CREATE DATABASE WechatDB")
#     print("Database 'WechatDB' created")
# 关闭游标和数据库连接
cursor.close()
db.close()

