import xml.etree.ElementTree as et

def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmldata = et.fromstring(web_data)
    msg_type = xmldata.find('MsgType').text
    if msg_type == 'text':
        return TextMsg(xmldata)
    else:
        return None


class Msg:
    def __init__(self, xmldata):
        self.ToUserName = xmldata.find('ToUserName').text
        self.FromUserName = xmldata.find('FromUserName').text
        self.CreateTime = xmldata.find('CreateTime').text
        self.MsgType = xmldata.find('MsgType').text
        self.MsgId = xmldata.find('MsgId').text


class TextMsg(Msg):
    def __init__(self, xmldata):
        Msg.__init__(self, xmldata)
        self.Content = xmldata.find('Content').text.encode('utf-8')






