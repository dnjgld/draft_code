from time import sleep
# import cv2
import pyautogui
import win32api
import win32con
import ctypes

MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA
    
n=2
while True:    

    sleep(0.1)
    win32api.keybd_event(0x51, MapVirtualKey(0x51, 0), 0, 0)
    sleep(0.1)
    win32api.keybd_event(0x51, MapVirtualKey(0x51, 0), win32con.KEYEVENTF_KEYUP, 0)
    
    for i in range(14):
        sleep(0.1)
        win32api.keybd_event(0x4b, MapVirtualKey(0x4b, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x4b, MapVirtualKey(0x4b, 0), win32con.KEYEVENTF_KEYUP, 0)

    # kkkkla
    
    sleep(0.1)
    win32api.keybd_event(0x49, MapVirtualKey(0x49, 0), 0, 0)

    sleep(0.40)
    win32api.keybd_event(0x4b, MapVirtualKey(0x4b, 0), 0, 0)
    
    sleep(0.1)
    win32api.keybd_event(0x4b, MapVirtualKey(0x4b, 0), win32con.KEYEVENTF_KEYUP, 0)

    sleep(0.1)
    win32api.keybd_event(0x49, MapVirtualKey(0x49, 0), win32con.KEYEVENTF_KEYUP, 0)
    
    temp = pyautogui.locateOnScreen('picture/results.png', confidence=0.9)
    if temp != None:
        sleep(10)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
        sleep(0.1)
        win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
        # press L

        sleep(2)
        if pyautogui.locateOnScreen('picture/refight.png', confidence=0.6)!= None:
            sleep(3)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
            # press L

            sleep(3)
            win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), win32con.KEYEVENTF_KEYUP, 0)     
            # press S  

            sleep(3)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
            # press L

        else:
            sleep(10)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
            # press L

            sleep(3)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
            # press L

            sleep(3)
            win32api.keybd_event(0x1B, MapVirtualKey(0x1B, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x1B, MapVirtualKey(0x1B, 0), win32con.KEYEVENTF_KEYUP, 0)
            # press esc

            sleep(3)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
            # press L 进

            # sleep(3)
            # win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), 0, 0)
            # sleep(0.1)
            # win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), win32con.KEYEVENTF_KEYUP, 0)     
            # # press S 
            
            # sleep(3)
            # win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), 0, 0)
            # sleep(0.1)
            # win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), win32con.KEYEVENTF_KEYUP, 0)     
            # # press S 

            sleep(3)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)   
            # press L 进任务

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
            win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), win32con.KEYEVENTF_KEYUP, 0)     
            # press S  

            sleep(3)
            win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), win32con.KEYEVENTF_KEYUP, 0)     
            # press S  

            # sleep(3)
            # win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), 0, 0)
            # sleep(0.1)
            # win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), win32con.KEYEVENTF_KEYUP, 0)     
            # # press S  

            sleep(3)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
            # press L 进easy
            
            for i in range(n):
                print(i)
            
                sleep(3)
                win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), 0, 0)
                sleep(0.1)
                win32api.keybd_event(0x53, MapVirtualKey(0x53, 0), win32con.KEYEVENTF_KEYUP, 0)     
                # press S 
            n+=1

            sleep(3)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
            # press L 确认任务

            sleep(3)
            win32api.keybd_event(0x41, MapVirtualKey(0x41, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x41, MapVirtualKey(0x41, 0), win32con.KEYEVENTF_KEYUP, 0)
            # press A 选是

            sleep(3)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
            # press L 确定

            sleep(5)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
            sleep(0.1)
            win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)
            # press L 选人
            
            # sleep(5)
            # win32api.keybd_event(0x09, MapVirtualKey(0x09, 0), 0, 0)
            # sleep(0.1)
            # win32api.keybd_event(0x09, MapVirtualKey(0x09, 0), win32con.KEYEVENTF_KEYUP, 0)     

            # sleep(3)
            # win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), 0, 0)
            # sleep(0.1)
            # win32api.keybd_event(0x4c, MapVirtualKey(0x4c, 0), win32con.KEYEVENTF_KEYUP, 0)     
            
# kikkkpwkkipwkkkikQKkkikkikkkkkkkkkkqkkkkkkkkkkklsslssla