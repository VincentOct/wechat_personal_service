# -*- coding: utf-8 -*-
# filename: main.py

import web
from handle import Handle

urls = (
    '/wx', 'Handle',
    '/', 'Hello'
)


class Hello:
    def Get(self):
        return 'Hello world.\nPower by python.'


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
