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
 
# 全屏幕截图
 
MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA
# kkkkkkkkkkk
# i=0
while True:
    # i+=1
    sleep(0.2)
    win32api.keybd_event(0x4b, MapVirtualKey(0x4b, 0), 0, 0)
    sleep(0.2)
    win32api.keybd_event(0x4b, MapVirtualKey(0x4b, 0), win32con.KEYEVENTF_KEYUP, 0)
    
    # temp = None
    # if (i%100==0): temp = pyautogui.locateOnScreen('picture/results.png', confidence=0.9)
    
    # # img = ImageGrab.grab(bbox=(0, 0, width, height))
    # # img.save('full_screen_img.jpg')
    # if temp != None:
    #     sleep(6)
    #     win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
    #     sleep(0.1)
    #     win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
        
    #     sleep(4)
    #     # img = ImageGrab.grab(bbox=(0, 0, width, height))
    #     # img.save('full_screen_img.jpg')
    #     if (pyautogui.locateOnScreen('picture/refight.png', confidence=0.5)!=None):
            
    #         print(1)

    #         sleep(3)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
    #         sleep(0.1)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)

    #         sleep(3)
    #         win32api.keybd_event(0x57, MapVirtualKey(0x57, 0), 0, 0)
    #         sleep(0.1)
    #         win32api.keybd_event(0x57, MapVirtualKey(0x57, 0), win32con.KEYEVENTF_KEYUP, 0)

    #         sleep(3)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
    #         sleep(0.1)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)

    #     else:
            
    #         print(2)

    #         sleep(10)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
    #         sleep(0.1)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
        
    #         sleep(3)
    #         win32api.keybd_event(0x1B, MapVirtualKey(0x1B, 0), 0, 0)
    #         sleep(0.1)
    #         win32api.keybd_event(0x1B, MapVirtualKey(0x1B, 0), win32con.KEYEVENTF_KEYUP, 0)

    #         sleep(3)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
    #         sleep(0.1)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)

    #         sleep(3)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
    #         sleep(0.1)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)   

    #         sleep(3)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
    #         sleep(0.1)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
            
    #         # 
    #         sleep(3)
    #         win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), 0, 0)
    #         sleep(0.1)
    #         win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), win32con.KEYEVENTF_KEYUP, 0)     

    #         sleep(3)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
    #         sleep(0.1)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)


    #         sleep(3)
    #         win32api.keybd_event(0x41, MapVirtualKey(0x41, 0), 0, 0)
    #         sleep(0.1)
    #         win32api.keybd_event(0x41, MapVirtualKey(0x41, 0), win32con.KEYEVENTF_KEYUP, 0)

    #         sleep(3)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
    #         sleep(0.1)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)

    #         sleep(5)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
    #         sleep(0.1)
    #         win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
    
    # sleep(0.1)    kkkk
    temp = pyautogui.locateOnScreen('picture/results.png', confidence=0.9)
    if temp != None:
        print(1)

        sleep(6)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)

        sleep(10)
        print("tab")
        win32api.keybd_event(0x09, MapVirtualKey(0x09, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x09, MapVirtualKey(0x09, 0), win32con.KEYEVENTF_KEYUP, 0)

        sleep(3)
        win32api.keybd_event(0x41, MapVirtualKey(0x41, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x41, MapVirtualKey(0x41, 0), win32con.KEYEVENTF_KEYUP, 0)
        # press A 选是

        sleep(3)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
        
        sleep(10)
        win32api.keybd_event(0x1B, MapVirtualKey(0x1B, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x1B, MapVirtualKey(0x1B, 0), win32con.KEYEVENTF_KEYUP, 0)

        sleep(3)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
        # press L 进

        sleep(3)
        win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), win32con.KEYEVENTF_KEYUP, 0)     
        # press S 

        sleep(3)
        win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), win32con.KEYEVENTF_KEYUP, 0)     
        # press S 

        sleep(3)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
        # press L 进

        sleep(3)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
        # press L 进

        sleep(3)
        win32api.keybd_event(0x41, MapVirtualKey(0x41, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x41, MapVirtualKey(0x41, 0), win32con.KEYEVENTF_KEYUP, 0)
        # press A 选是   

        sleep(3)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
        # press L 进

        sleep(10)
        print("tab")
        win32api.keybd_event(0x09, MapVirtualKey(0x09, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x09, MapVirtualKey(0x09, 0), win32con.KEYEVENTF_KEYUP, 0)

        sleep(3)
        win32api.keybd_event(0x41, MapVirtualKey(0x41, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x41, MapVirtualKey(0x41, 0), win32con.KEYEVENTF_KEYUP, 0)
        # press A 选是   

        sleep(3)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
        # press L 进

        sleep(10)
        print("tab")
        win32api.keybd_event(0x09, MapVirtualKey(0x09, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x09, MapVirtualKey(0x09, 0), win32con.KEYEVENTF_KEYUP, 0)

        sleep(3)
        win32api.keybd_event(0x41, MapVirtualKey(0x41, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x41, MapVirtualKey(0x41, 0), win32con.KEYEVENTF_KEYUP, 0)
        # press A 选是   

        sleep(3)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
        # press L 进

# 