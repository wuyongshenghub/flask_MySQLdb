# encoding:utf-8
# dbutil.py

import os
import sys
import MySQLdb

# 将项目文件夹加入到sys.paht.append()中
from os.path import join, dirname, abspath, exists
code_home = dirname(dirname(abspath(__file__)))
code_conf = join(code_home, 'conf')
sys.path.append(code_home)
# print code_home, code_conf  # sys.path
from conf.config import mysqlConnection

# print mysqlConnection.get('host')
# print mysqlConnection.get('port')
# print mysqlConnection.get('user')
# print mysqlConnection.get('passwd')
# print mysqlConnection.get('db')
# print mysqlConnection.get('charset', None)


class DB(object):
    """封装与操作常用的数据库，初始化数据库等"""

    def __init__(self):
        try:
            self.conn = MySQLdb.connect(host=mysqlConnection.get('host'), port=mysqlConnection.get('port'), user=mysqlConnection.get(
                'user'), passwd=mysqlConnection.get('passwd'), db=mysqlConnection.get('db'), charset='utf8')
            # print 'success'
            # 数据库自动提交
            self.conn.autocommit(True)
        except Exception, e:
            # logger.error(e)
            print e
            sys.exit()

    def execute(self, sql):
        # SQL 执行
        try:
            # 执行游标
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except (AttributeError, MySQLdb.OperationalError):
            try:
                # 关闭游标 数据库conn
                cursor.close()
                self.conn.close()
            except:
                pass
        # 返回游标
        return cursor

# db = DB()
# db
