import cv2
import subprocess
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import threading
import shlex
import numpy as np
import sys
import os

# 示例直播流URLs（这些可能已过期）
DEFAULT_STREAMS = [
    "https://d1--ov-gotcha207.bilivideo.com/live-bvc/905486/live_50329118_9516950_1500/index.m3u8?expires=1715345578&len=0&oi=2906794593&pt=h5&qn=0&trid=1007ccf13453088e40f18b4a83cc7f31ec6f&sigparams=cdn,expires,len,oi,pt,qn,trid&cdn=ov-gotcha207&sign=d98f874618893a7181a2eaa9c172a5a2&sk=c631df6078f80f4f3f7f34bf7bdec842&p2p_type=4294967295&sl=10&free_type=0&mid=0&pp=rtmp&source=onetier&trace=0&site=1e19dc7e5e2a50b639b0770667ce21d8&order=1",
]

class StreamPlayer:
    def __init__(self):
        self.root = Tk()
        self.root.title("多直播流播放器")
        self.root.geometry("800x600")
        
        # 播放器状态
        self.players = []
        self.is_playing = {}
        
        self.setup_ui()
    
    def setup_ui(self):
        # 顶部控制面板
        control_frame = Frame(self.root)
        control_frame.pack(fill=X, padx=10, pady=5)
        
        Button(control_frame, text="添加直播流", command=self.add_stream).pack(side=LEFT, padx=5)
        Button(control_frame, text="从文件加载URL", command=self.load_urls_from_file).pack(side=LEFT, padx=5)
        Button(control_frame, text="停止所有", command=self.stop_all).pack(side=LEFT, padx=5)
        
        # URL输入框
        url_frame = Frame(self.root)
        url_frame.pack(fill=X, padx=10, pady=5)
        
        Label(url_frame, text="直播流URL:").pack(side=LEFT)
        self.url_entry = Entry(url_frame, width=50)
        self.url_entry.pack(side=LEFT, fill=X, expand=True, padx=5)
        Button(url_frame, text="播放", command=self.play_url).pack(side=RIGHT)
        
        # 播放器容器
        self.player_frame = Frame(self.root)
        self.player_frame.pack(fill=BOTH, expand=True, padx=10, pady=5)
        
        # 状态栏
        self.status_var = StringVar()
        self.status_var.set("就绪")
        status_bar = Label(self.root, textvariable=self.status_var, relief=SUNKEN, anchor=W)
        status_bar.pack(side=BOTTOM, fill=X)
    
    def add_stream(self):
        """添加默认直播流"""
        if DEFAULT_STREAMS:
            self.play_stream(DEFAULT_STREAMS[0])
        else:
            messagebox.showinfo("提示", "请在URL输入框中输入直播流地址")
    
    def load_urls_from_file(self):
        """从文件加载URL列表"""
        file_path = filedialog.askopenfilename(
            title="选择URL文件",
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                for url in urls[:3]:  # 最多加载3个
                    self.play_stream(url)
            except Exception as e:
                messagebox.showerror("错误", f"读取文件失败: {str(e)}")
    
    def play_url(self):
        """播放输入框中的URL"""
        url = self.url_entry.get().strip()
        if url:
            self.play_stream(url)
        else:
            messagebox.showwarning("警告", "请输入直播流URL")
    
    def play_stream(self, video_url):
        """播放指定的视频流"""
        if len(self.players) >= 4:  # 最多4个播放器
            messagebox.showwarning("警告", "最多只能同时播放4个流")
            return
        
        player_id = len(self.players)
        self.status_var.set(f"正在连接流 {player_id + 1}...")
        
        # 创建播放器窗口
        player_window = Toplevel(self.root)
        player_window.title(f"直播流 {player_id + 1}")
        player_window.geometry("640x480")
        
        label = Label(player_window, text="正在加载...", bg="black", fg="white")
        label.pack(fill=BOTH, expand=True)
        
        # 添加控制按钮
        control_frame = Frame(player_window)
        control_frame.pack(fill=X)
        Button(control_frame, text="停止", command=lambda: self.stop_player(player_id)).pack(side=LEFT)
        
        self.players.append({
            'window': player_window,
            'label': label,
            'url': video_url,
            'thread': None
        })
        
        self.is_playing[player_id] = True
        
        # 启动播放线程
        thread = threading.Thread(target=self.read_from_ffmpeg, args=(player_id, video_url))
        thread.daemon = True
        self.players[player_id]['thread'] = thread
        thread.start()
        
        self.status_var.set(f"已启动流 {player_id + 1}")
    
    def stop_player(self, player_id):
        """停止指定播放器"""
        if player_id < len(self.players):
            self.is_playing[player_id] = False
            self.players[player_id]['window'].destroy()
            self.status_var.set(f"已停止流 {player_id + 1}")
    
    def stop_all(self):
        """停止所有播放器"""
        for i in range(len(self.players)):
            if i in self.is_playing:
                self.is_playing[i] = False
        for player in self.players:
            try:
                player['window'].destroy()
            except:
                pass
        self.players.clear()
        self.is_playing.clear()
        self.status_var.set("已停止所有播放")
    
    def get_video_resolution(self, video_url):
        """获取视频分辨率"""
        command = f"ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {shlex.quote(video_url)}"
        try:
            proc = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, errors = proc.communicate(timeout=10)
            if proc.returncode == 0:
                dimensions = output.strip().split('x')
                if len(dimensions) == 2:
                    return int(dimensions[0]), int(dimensions[1])
            return 640, 480  # 默认分辨率
        except Exception as e:
            print(f"分辨率获取失败: {e}")
            return 640, 480
    
    def read_from_ffmpeg(self, player_id, video_url):
        """从FFmpeg读取视频流"""
        if player_id >= len(self.players):
            return
        
        label = self.players[player_id]['label']
        
        try:
            width, height = self.get_video_resolution(video_url)
            
            command = [
                'ffmpeg',
                '-i', video_url,
                '-pix_fmt', 'bgr24',
                '-vcodec', 'rawvideo',
                '-an', '-sn',
                '-f', 'image2pipe', '-'
            ]
            
            pipe = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=10**8)
            
            while self.is_playing.get(player_id, False):
                num_bytes = width * height * 3
                raw_image = pipe.stdout.read(num_bytes)
                
                if not raw_image:
                    break
                
                if len(raw_image) != num_bytes:
                    continue
                
                try:
                    image = np.frombuffer(raw_image, dtype='uint8').reshape((height, width, 3))
                    img = Image.fromarray(image)
                    
                    # 调整图像大小以适应窗口
                    img = img.resize((640, 480), Image.Resampling.LANCZOS)
                    
                    imgtk = ImageTk.PhotoImage(image=img)
                    
                    # 更新UI（需要在主线程中执行）
                    self.root.after(0, lambda: self.update_image(label, imgtk))
                    
                except Exception as e:
                    print(f"图像处理错误: {e}")
                    continue
            
            pipe.terminate()
            
        except Exception as e:
            error_msg = f"播放错误: {str(e)}"
            print(error_msg)
            self.root.after(0, lambda: label.config(text=error_msg))
    
    def update_image(self, label, imgtk):
        """更新图像显示"""
        try:
            label.config(image=imgtk)
            label.image = imgtk  # 保持引用
        except:
            pass  # 窗口可能已关闭
    
    def run(self):
        """启动应用"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def on_closing(self):
        """窗口关闭事件"""
        self.stop_all()
        self.root.destroy()

if __name__ == "__main__":
    # 检查ffmpeg是否可用
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except:
        print("错误: 未找到ffmpeg，请确保已安装ffmpeg并添加到PATH")
        sys.exit(1)
    
    app = StreamPlayer()
    app.run()