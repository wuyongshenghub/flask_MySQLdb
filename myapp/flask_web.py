# encoding:utf-8

from method.select import DBOperation  # 导入类名
from conf.config import host, port
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/userlist')
def userlist():
    with open('data.txt', 'r') as f:
        html_str = '<table border=1>'
        for l in f:
            html_str += '<tr><td>%s</td><td>%s</td></tr>' % (
                tuple(l.strip().split(':')))
        html_str += '</table>'
    return html_str


@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    if request.method == 'GET':
        return render_template('adduser.html')
    elif request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        return 'username is %s and password is %s' % (user, pwd)


@app.route('/showlist')
def showlist():
	# 查询DB 数据 web页面展现
    # x = DBOperation()
    # print x.select()
    return render_template('showlist.html', data=DBOperation().select())


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
