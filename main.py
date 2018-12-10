# -*- coding: utf-8 -*-
# filename: main.py

import web
# from handle import

urls = (
    '/wx', 'Handle'
)


class Handle:
    def GET(self):  # 此处的 get 即 http 中的 get 方法。
        return 'Hello, this is a text msg.'


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
