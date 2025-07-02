from time import sleep
# import cv2
# import pyautogui
import win32api
import win32con
import ctypes

MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA

num = 87
while True:
    sleep(0.2)
    win32api.keybd_event(num, MapVirtualKey(num, 0), 0, 0)
    sleep(0.1)
    win32api.keybd_event(num, MapVirtualKey(num, 0), win32con.KEYEVENTF_KEYUP, 0)
    
    if num == 100:
        break

# wwwwwwwwwww