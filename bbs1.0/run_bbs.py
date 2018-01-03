#!/usr/bin/env python
# encoding: utf-8

"""
@author: dxy

"""

from flask import Flask  #
from flask import render_template  # 读取模板
from flask import request  # 客户端发送的请求
from flask import redirect  # 重定向
import time

# 初始化一个 Flask 实例
app = Flask(__name__)


message_list = []
@app.route('/', methods=['GET'])
def hello_world():
    return '<h1>盖伦的留言板</h1>'


@app.route('/message')
def message_view():
    print '请求方法', request.method
    print 'request, query 参数', request.args
    return render_template('message_index.html', messages=message_list)


@app.route('/message/add', methods=['POST'])
def message_add():
    print 'message_add 请求方法', request.method
    print 'request, POST 的 form 表单数据', request.form
    msg = {'abc': request.form.get('msg_post', '')}
    message_list.append(msg)

    return redirect('/message')


# 运行服务器
if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2001,
    )
    app.run(**config)
