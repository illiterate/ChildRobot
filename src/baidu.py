from aip import AipSpeech

""" 你的 APPID AK SK ，去百度云申请服务"""
APP_ID = 'xxxxxxxx'				#你的APP_ID
API_KEY = 'xxxxxxxxxxxxxxxx'			#你的API_KEY
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxx'	#你的SECRET_KEY
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

#语音识别，返回识别结果
def recognition():
    # 读取文件
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    #   识别本地文件
    d = client.asr(get_file_content('output.wav'), 'wav', 16000, {
        'lan': 'zh',
    })
    word = d['result'][0]
    print(word)
    return word

#语音合成，生成语音文件
def synthesis(text):
    result  = client.synthesis(text, 'zh', 1, {
        'vol': 5,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)