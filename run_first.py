#!/usr/bin/env python
# encoding: utf-8
"""
@author: dxy

"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello, World！我是盖特曼<h1>"


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=1024,  # 1024以内的端口是保留端口，有管理员权限才能用
        threaded=True  # 实现多线程服务,优化性能
    )
    app.run(**config)
