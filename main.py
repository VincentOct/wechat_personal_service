# -*- coding: utf-8 -*-
# filename: main.py

import web

urls = (
    '/wx', 'Handle'
)


class Handle:
    def GET(self):
        return 'Hello, this is a text msg.'


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
