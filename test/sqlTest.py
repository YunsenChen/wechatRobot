# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import MySQLdb
# 解决出现的写入错误



print('连接到mysql服务器...')
conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123mysql', db='onefive', charset='utf8')
print('连接上了!')
cur = conn.cursor()
# 判断表是否存在，若存在则删除此表
cur.execute("DROP TABLE IF EXISTS AGENT")
# 创建表
sql = """CREATE TABLE test(
                 title  CHAR(20),
                 sec_title  CHAR(20),
                 content  VARCHAR(6499))"""
cur.execute(sql)
conn.commit()
conn.close()
