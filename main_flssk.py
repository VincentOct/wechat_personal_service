# -*- coding:utf8 -*-

import hashlib
from flask import Flask, request, make_response
import time


app = Flask(__name__)
# app.debug = True


@app.route('/greeting', methods=['GET'])
def greeting():
    return 'Hello! This is my wechat service. | [Power by Flask]'


@app.route('/wx', methods=['GET'])
def wechat_check():
    if request.method == 'GET':
        token = 'zhangyu'
        args = request.args
        signature = args.get('signature', '')
        timestamp = args.get('timestamp', '')
        nonce = args.get('nonce', '')
        echostr = args.get('echostr', '')
        alist = [token, timestamp, nonce]
        alist.sort()
        raw_str = ''.join(alist)
        sha1 = hashlib.sha1()
        sha1.update(raw_str.encode('utf-8'))
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return make_response(echostr)
        else:
            return None


if __name__ == '__main__':
    app.run()


