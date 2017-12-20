import recorder
import baidu
import robot
import play

if __name__ == '__main__':
    print("Child Robot语音助手为您服务...")
    while True:
        a = input('按Enter键继续...')
        if(a == ''):
            recorder.recode(5)
            question = baidu.recognition()
            answer = robot.getAnswer(question)
            baidu.synthesis(answer)
            play.playAudio()
        else:
            break
    print("谢谢...")