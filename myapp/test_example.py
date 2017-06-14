# encoding:utf-8
# test_example.py

# 装饰器 @property


class Student(object):
    @property #它可以将方法变成属性,让get和set方法更好用
    def testname(self):
        return self.name

    @testname.setter
    def testname(self, name):
        self.name = name

ss = Student()
ss.testname = 'alex'
print ss.testname
