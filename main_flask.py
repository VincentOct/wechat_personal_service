# -*- coding:utf8 -*-

import hashlib
from flask import Flask, request, make_response
from xml.etree import ElementTree as ET
import time


app = Flask(__name__)
# app.debug = True


@app.route('/greeting', methods=['GET'])
def greeting():
    return 'Hello! This is my wechat service. | [Power by Flask]'


@app.route('/wx', methods=['GET', 'POST'])
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
    if request.method == 'POST':
        print(request.data)
        xml_recv = ET.fromstring(request.data)
        to_user = xml_recv.find("ToUserName").text
        from_user = xml_recv.find("FromUserName").text
        content = xml_recv.find("Content").text
        print(to_user, from_user, content)
        reply_str = """<xml> 
        <ToUserName>< ![CDATA[{to_user}] ]></ToUserName> 
        <FromUserName>< ![CDATA[{from_user}] ]></FromUserName> 
        <CreateTime>{createtime}</CreateTime> 
        <MsgType>< ![CDATA[text] ]></MsgType> 
        <Content>< ![CDATA[{content}] ]></Content> 
        </xml>"""
        reply_xml = reply_str.format(to_user=from_user, from_user=to_user,
                                     createtime=int(time.time()), content=content)
        response = make_response(reply_xml)
        response.content_type = 'application/xml'
        return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

