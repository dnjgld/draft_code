import pyautogui
import time
import os
from PIL import Image

def zan():
    time.sleep(0.5)    # 等待 0.5 秒
    if pyautogui.locateOnScreen('picture/zan.png', confidence=0.7) != None:
        left, top, width, height = pyautogui.locateOnScreen('picture/zan.png', confidence=0.7)   # 寻找 点赞图片；
        center = pyautogui.center((left, top, width, height))    # 寻找 图片的中心
        pyautogui.click(center)    # 点击
    else:
        pyautogui.scroll(-500)    # 本页没有图片后，滚动鼠标；
        print('没有找到目标，屏幕下滚~')

while True:
    zan()   # 调用点赞函数


