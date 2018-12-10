import hashlib


signature = '9bae1fb83f86605842a0e1c89e015419c56577a0'
timestamp = '1544459850'
nonce = '439441622'
echostr = ''
token = 'hello2019'
alist = [token, timestamp, nonce]
alist.sort()
rawstr = ''.join(alist)

print('rawstr:', rawstr)


sha1 = hashlib.sha1()
sha1.update(rawstr.encode('utf-8'))
hashcode = sha1.hexdigest()
print(hashcode == signature)
# print(hashcode)
