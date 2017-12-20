# 前言
> 买来树莓派后，一直放在桌子上吃灰了。
> 马上到年底了，也不知道给小外甥、小侄女送什么礼物。
> 那天室友说拿树莓派做个聊天机器人送人吧! 想了想完全可以用树莓派 + Python给小孩做个问答机器人， 所以顶着期末复习的压力，做出了这个智障小助手。

# 主要功能
> 利用百度语音和图灵机器人的API做了个简单的智障聊天机器人，主要功能有：生活百科、天气查询、数字计算、问答百科、中英互译、聊天对话（笑话、故事、星座、绕口令）等。

# 1.安装sox
由于开发环境是Linux，所以不能用mp3play库来播放音乐，找来找去还是sox比较好用。
> sudo apt-get install sox
> sudo apt-get install sox libsox-fmt-all

# 2.安装pyaudio
用pip安装pyaudio时报错，缺少portaudio.h。在网上查了查用下面的命令安装不会报错。
> sudo apt-get install python-pyaudio python3-pyaudio

# 3.安装百度语音的Python SDK
直接用pip安装就好。
> sudo pip3 install baidu-aip

# 使用
> 由于我把我的API隐藏了，所以你们需要先在百度开放平台和图灵机器人去申请账号和API，在源文件中相应的位置补充上，再利用Python开发平台运行main.py就好。

![](http://img02.sogoucdn.com/app/a/100520146/13b6a416935eb4f37929e53f419f504f)
