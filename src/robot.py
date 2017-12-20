import urllib.request
import urllib.parse
import json
def getAnswer(question):
    url = 'http://www.tuling123.com/openapi/api'
    data =  {
            'key':'xxxxxxxxxxxxxxxxxx',             #去图灵机器人申请
            'info':question, 
            #'loc':'北京市中关村',
            'userid':'xxx'                      #自定义
            }
    data=urllib.parse.urlencode(data).encode('utf-8')
    res = urllib.request.Request(url, data = data)
    info = urllib.request.urlopen(res)
    answer = json.loads(info.read().decode('utf-8'))['text']
    print(answer)
    return answer