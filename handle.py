# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web


# _token = input('Enter the token.')


class Handle:
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return 'Hello, this is a handle view page.'
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = 'hello2019'
            alist = [token, timestamp, nonce]
            alist.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, alist)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as e:
            return e



