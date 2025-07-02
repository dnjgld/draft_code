
from time import sleep
# import cv2
import pyautogui
import win32api
import win32con
import ctypes
from PIL import ImageGrab
 
# 获取当前分辨率下的屏幕尺寸
 
width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

print(width)
print(height)
# 全屏幕截图
 
MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA

while True:
    temp = pyautogui.locateOnScreen('C:/Users/D0828/Desktop/files/picture/continue.png', confidence=0.7)
    if temp != None:
        print(1)
        center = pyautogui.center(temp)
        pyautogui.click(center)
        
    temp = pyautogui.locateOnScreen('C:/Users/D0828/Desktop/files/picture/fight.png', confidence=0.7)    
    if temp != None:
        print(1)
        center = pyautogui.center(temp)
        pyautogui.click(center) 

    temp = pyautogui.locateOnScreen('C:/Users/D0828/Desktop/files/picture/close.png', confidence=0.7)    
    if temp != None:
        print(1)
        center = pyautogui.center(temp)
        pyautogui.click(center)
        
    temp = pyautogui.locateOnScreen('C:/Users/D0828/Desktop/files/picture/accept.png', confidence=0.7)    
    if temp != None:
        print(1)
        center = pyautogui.center(temp)
        pyautogui.click(center)
          
    temp = pyautogui.locateOnScreen('C:/Users/D0828/Desktop/files/picture/return.png', confidence=0.7)    
    if temp != None:
        print(1)
        center = pyautogui.center(temp)
        pyautogui.click(center)
    
    temp = pyautogui.locateOnScreen('C:/Users/D0828/Desktop/files/picture/error1.png', confidence=0.9)    
    if temp != None:
        print(1)
        center = pyautogui.center(temp)
        pyautogui.click(center)
    
