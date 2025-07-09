# import tkinter as tk
# import pyautogui
# import cv2
# import numpy as np
# from PIL import ImageGrab
# import time

# class ImageDetection:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("图像间隔检测")
#         self.label = tk.Label(root, text="", font=("Helvetica", 20))
#         self.label.pack(pady=20)
#         self.template1 = cv2.imread('image1.png', 0)
#         self.template2 = cv2.imread('image2.png', 0)
#         self.last_detection_time = None
#         self.intervals = []
#         self.detect_image1()

#     def detect_image1(self):
#         screen = np.array(ImageGrab.grab(bbox=None))  # 捕获全屏
#         screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        
#         # 检测第一个图像
#         result1 = cv2.matchTemplate(screen_gray, self.template1, cv2.TM_CCOEFF_NORMED)
#         threshold = 0.8
#         loc1 = np.where(result1 >= threshold)
        
#         if len(loc1[0]) > 0:
#             self.last_detection_time = time.time()
#             self.label.config(text="检测到 Image1")
#             self.root.after(1, self.detect_image2)  # 1秒后开始检测第二个图像
#         else:
#             self.root.after(1, self.detect_image1)  # 每秒检查一次

#     def detect_image2(self):
#         screen = np.array(ImageGrab.grab(bbox=None))  # 捕获全屏
#         screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        
#         # 检测第二个图像
#         result2 = cv2.matchTemplate(screen_gray, self.template2, cv2.TM_CCOEFF_NORMED)
#         threshold = 0.8
#         loc2 = np.where(result2 >= threshold)
        
#         if len(loc2[0]) > 0 and self.last_detection_time:
#             current_time = time.time()
#             interval = current_time - self.last_detection_time
#             self.intervals.append(interval)
#             avg_interval = sum(self.intervals) / len(self.intervals)
#             self.label.config(text=f"检测到 Image2, 当前间隔: {interval:.2f} 秒, 平均间隔: {avg_interval:.2f} 秒")
#             self.last_detection_time = None  # 重置检测时间
#             self.root.after(1, self.detect_image1)  # 1秒后重新检测第一个图像
#         else:
#             self.root.after(1, self.detect_image2)  # 每秒检查一次

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ImageDetection(root)
#     root.mainloop()

import tkinter as tk
import cv2
import numpy as np
from PIL import ImageGrab
import time
import os
from tkinter import filedialog, messagebox

class ImageDetection:
    def __init__(self, root):
        self.root = root
        self.root.title("图像持续时间检测")
        self.label = tk.Label(root, text="请选择要检测的图像", font=("Helvetica", 16))
        self.label.pack(pady=20)
        
        # 添加选择图像按钮
        self.select_button = tk.Button(root, text="选择模板图像", command=self.select_template, font=("Helvetica", 12))
        self.select_button.pack(pady=10)
        
        # 添加开始检测按钮
        self.start_button = tk.Button(root, text="开始检测", command=self.start_detection, font=("Helvetica", 12))
        self.start_button.pack(pady=10)
        self.start_button.config(state='disabled')
        
        self.template = None
        self.image_start_time = None
        self.is_detecting = False
        
    def select_template(self):
        file_path = filedialog.askopenfilename(
            title="选择模板图像",
            filetypes=[("图像文件", "*.png *.jpg *.jpeg *.bmp *.gif"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                self.template = cv2.imread(file_path, 0)
                if self.template is not None:
                    self.label.config(text=f"已选择模板图像: {os.path.basename(file_path)}")
                    self.start_button.config(state='normal')
                else:
                    messagebox.showerror("错误", "无法读取图像文件，请检查文件格式")
            except Exception as e:
                messagebox.showerror("错误", f"读取图像时出错: {str(e)}")
    
    def start_detection(self):
        if self.template is not None:
            self.is_detecting = True
            self.start_button.config(state='disabled')
            self.select_button.config(state='disabled')
            self.detect_image()

    def detect_image(self):
        if not self.is_detecting or self.template is None:
            return
            
        try:
            screen = np.array(ImageGrab.grab(bbox=None))  # 捕获全屏
            screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            
            # 检测图像
            result = cv2.matchTemplate(screen_gray, self.template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(result >= threshold)
            
            if len(loc[0]) > 0:
                if self.image_start_time is None:
                    self.image_start_time = time.time()
                    self.label.config(text="检测到图像")
                else:
                    current_time = time.time()
                    duration = current_time - self.image_start_time
                    self.label.config(text=f"图像保持时间: {duration:.2f} 秒")
            else:
                if self.image_start_time is not None:
                    current_time = time.time()
                    duration = current_time - self.image_start_time
                    self.label.config(text=f"图像已消失，持续时间: {duration:.2f} 秒")
                    self.image_start_time = None
                    
        except Exception as e:
            self.label.config(text=f"检测过程中出错: {str(e)}")
            self.is_detecting = False
            self.start_button.config(state='normal')
            self.select_button.config(state='normal')
            return
        
        if self.is_detecting:
            self.root.after(100, self.detect_image)  # 每0.1秒检查一次

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageDetection(root)
    root.mainloop()
