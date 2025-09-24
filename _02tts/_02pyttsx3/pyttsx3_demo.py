import pyttsx3

'''
window安装TTS引擎
无需处理，一般默认支持

linux（debian系列）安装TTS引擎
sudo apt update && sudo apt install espeak-ng libespeak1

macOS安装TTS引擎
'''

if __name__ == "__main__":
    # 初始化语音引擎
    engine = pyttsx3.init()

    # 设置要说的文本
    text = "您好，我是一直可爱的小猪！"

    # 设置语速,默认值是200
    engine.setProperty('rate', 200)

    # 设置音量,默认值是1.0
    engine.setProperty('volume', 1.0)

    # 保存到文件
    engine.save_to_file(text, 'test.wav')
    engine.runAndWait()