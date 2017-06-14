# encoding:utf-8
import sys
import os
from os.path import join, dirname, abspath
code_home = dirname(dirname(abspath(__file__)))
code_db = join(code_home, 'db')
sys.path.append(code_home)

# print code_db, code_home
from db import dbutil
mysql = dbutil.DB()


class DBOperation(object):
    def select(self):
        sql = "select * from a"
        cursor = mysql.execute(sql)
        data = cursor.fetchall()
        return data
