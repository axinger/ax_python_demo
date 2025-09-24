# _*_ coding: utf-8 _*_
# @Time : 2024/3/19 21:03
# @Author : Michael
# @File : edgeTTS.py
# @desc :
import asyncio
import random
import edge_tts


async def tts() -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():  # 流式获取
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                print(f"WordBoundary: {chunk}")

async def search_voice_tts() -> None:
    # 根据条件获取语音列表
    voices = await edge_tts.VoicesManager.create()
    # 查找男性、中文、中国大陆的语音
    voice = voices.find(Gender="Male", Language="zh", Locale="zh-CN")
    print(voice)
    # 在查找的结果中随机选择语音
    selected_voice = random.choice(voice)["Name"]
    print(selected_voice)
    communicate = edge_tts.Communicate(TEXT, random.choice(voice)["Name"])
    await communicate.save(OUTPUT_FILE)

async def tts_with_submaker() -> None:
    """输出字幕"""
    communicate = edge_tts.Communicate(TEXT, VOICE)
    submaker = edge_tts.SubMaker()
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])

    with open(WEBVTT_FILE, "w", encoding="utf-8") as file:
        file.write(submaker.generate_subs())


'''
利用微软的免费文本转语音API服务
微软已禁止国内访问这个服务，需要外网环境
一键安装，转换速度快，质量较好，可控选项多
开源地址：https://github.com/rany2/edge-tts

zh-CN-XiaoxiaoNeural - 女声，自然
zh-CN-YunxiNeural - 男声，自然
zh-CN-YunyangNeural - 男声，新闻播报风格
zh-CN-XiaoxuanNeural - 女声，成熟
zh-CN-YunxiaNeural - 男声，少年
zh-CN-YunjianNeural - 男声，播报解说风格
zh-HK-WanLungNeural - 男生，粤语
'''


if __name__ == "__main__":
    TEXT = "微软的 edge tts 好棒啊!"
    VOICE = "zh-CN-YunyangNeural"  # ShortName
    OUTPUT_FILE = "test1.mp3"
    WEBVTT_FILE = "test.vtt"
    # 列出相关的voice
    voices_options = asyncio.run(edge_tts.list_voices())
    voices_options = [voice for voice in voices_options if voice["Locale"].startswith("zh-")]
    print(voices_options)
    # 调用 tts
    asyncio.run(tts())
    # 调用 search_voice_tts, 随机选择语音
    asyncio.run(search_voice_tts())
    # 调用 tts_with_submaker, 生成字幕
    asyncio.run(tts_with_submaker())
