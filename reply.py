import time


class Msg:
    def __init__(self):
        pass

    def send(self):
        return 'Success'


class TextMsg(Msg):
    def __init__(self, to_user_name, from_user_name, content):
        super().__init__()
        self.info_dict = {
            'ToUserName': to_user_name,
            'FromUserName': from_user_name,
            'CreateTime': int(time.time()),
            'Content': content
        }

    def send(self):
        xmlform = '''<xml> <ToUserName>< ![CDATA[{ToUserName}] ]></ToUserName> <FromUserName>< ![CDATA[{FromUserName}]]></FromUserName> <CreateTime>{CreateTime}</CreateTime> <MsgType>< ![CDATA[text] ]></MsgType> <Content>< ![CDATA[{Content}] ]></Content> </xml> '''
        return xmlform.format(**self.info_dict)
