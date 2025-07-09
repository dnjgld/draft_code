# B站直播流获取和播放器 - 整合版
import requests
import subprocess
from tkinter import *
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import threading
import shlex
import numpy as np
import sys

class BiliBiliLivePlayer:
    def __init__(self):
        self.root = Tk()
        self.root.title("B站直播流播放器")
        self.root.geometry("900x700")
        
        # 播放器状态
        self.players = []
        self.is_playing = {}
        
        self.setup_ui()
    
    def setup_ui(self):
        # 顶部控制面板
        control_frame = Frame(self.root)
        control_frame.pack(fill=X, padx=10, pady=10)
        
        # B站直播间输入
        bilibili_frame = LabelFrame(control_frame, text="B站直播间", padx=10, pady=10)
        bilibili_frame.pack(fill=X, pady=5)
        
        room_frame = Frame(bilibili_frame)
        room_frame.pack(fill=X)
        
        Label(room_frame, text="房间号:").pack(side=LEFT)
        self.room_entry = Entry(room_frame, width=20)
        self.room_entry.pack(side=LEFT, padx=5)
        Button(room_frame, text="获取并播放", command=self.get_and_play_bilibili, bg="#00a1d6", fg="white").pack(side=LEFT, padx=5)
        
        # 直接URL输入
        url_frame = LabelFrame(control_frame, text="直接播放URL", padx=10, pady=10)
        url_frame.pack(fill=X, pady=5)
        
        url_input_frame = Frame(url_frame)
        url_input_frame.pack(fill=X)
        
        Label(url_input_frame, text="直播流URL:").pack(side=LEFT)
        self.url_entry = Entry(url_input_frame, width=50)
        self.url_entry.pack(side=LEFT, fill=X, expand=True, padx=5)
        Button(url_input_frame, text="播放", command=self.play_url).pack(side=RIGHT)
        
        # 控制按钮
        Button(control_frame, text="停止所有播放", command=self.stop_all, bg="#ff6b6b", fg="white").pack(pady=5)
        
        # 播放器列表显示
        list_frame = LabelFrame(self.root, text="当前播放列表", padx=10, pady=10)
        list_frame.pack(fill=X, padx=10, pady=5)
        
        self.player_listbox = Listbox(list_frame, height=6)
        self.player_listbox.pack(fill=X, pady=5)
        
        # 状态栏
        self.status_var = StringVar()
        self.status_var.set("就绪 - 请输入B站房间号或直播流URL")
        status_bar = Label(self.root, textvariable=self.status_var, relief=SUNKEN, anchor=W)
        status_bar.pack(side=BOTTOM, fill=X)
    
    def get_and_play_bilibili(self):
        """获取B站直播流并播放"""
        room_id = self.room_entry.get().strip()
        if not room_id:
            messagebox.showwarning("警告", "请输入B站直播房间号")
            return
        
        self.status_var.set(f"正在获取房间 {room_id} 的直播流...")
        
        # 在新线程中获取直播流URL
        threading.Thread(target=self._fetch_bilibili_stream, args=(room_id,), daemon=True).start()
    
    def _fetch_bilibili_stream(self, room_id):
        """在后台线程获取B站直播流"""
        try:
            result = self.get_real_url(room_id)
            if result:
                # 让用户选择线路
                self.root.after(0, lambda: self._show_stream_selection(room_id, result))
            else:
                self.root.after(0, lambda: self.status_var.set(f"获取房间 {room_id} 的直播流失败"))
        except Exception as e:
            error_msg = f"错误: {str(e)}"
            self.root.after(0, lambda msg=error_msg: self.status_var.set(msg))
    
    def _show_stream_selection(self, room_id, streams):
        """显示线路选择对话框"""
        if len(streams) == 1:
            # 只有一个线路，直接播放
            url = list(streams.values())[0]
            self.play_stream(url, f"房间{room_id}")
        else:
            # 多个线路，让用户选择
            selection_window = Toplevel(self.root)
            selection_window.title(f"选择播放线路 - 房间{room_id}")
            selection_window.geometry("600x400")
            selection_window.grab_set()  # 模态对话框
            
            Label(selection_window, text=f"检测到 {len(streams)} 个可用线路，请选择:", font=("Arial", 12)).pack(pady=10)
            
            # 线路列表
            listbox = Listbox(selection_window, height=10)
            listbox.pack(fill=BOTH, expand=True, padx=20, pady=10)
            
            urls = []
            for name, url in streams.items():
                listbox.insert(END, f"{name}: {url[:80]}...")
                urls.append((name, url))
            
            # 按钮
            button_frame = Frame(selection_window)
            button_frame.pack(pady=10)
            
            def play_selected():
                selection = listbox.curselection()
                if selection:
                    idx = selection[0]
                    name, url = urls[idx]
                    self.play_stream(url, f"房间{room_id}-{name}")
                    selection_window.destroy()
                else:
                    messagebox.showwarning("警告", "请选择一个线路")
            
            def play_all():
                for name, url in urls:
                    self.play_stream(url, f"房间{room_id}-{name}")
                selection_window.destroy()
            
            Button(button_frame, text="播放选中线路", command=play_selected, bg="#00a1d6", fg="white").pack(side=LEFT, padx=5)
            Button(button_frame, text="播放所有线路", command=play_all, bg="#ff9500", fg="white").pack(side=LEFT, padx=5)
            Button(button_frame, text="取消", command=selection_window.destroy).pack(side=LEFT, padx=5)
    
    def play_url(self):
        """播放输入框中的URL"""
        url = self.url_entry.get().strip()
        if url:
            self.play_stream(url, "自定义URL")
        else:
            messagebox.showwarning("警告", "请输入直播流URL")
    
    def play_stream(self, video_url, stream_name):
        """播放指定的视频流"""
        if len(self.players) >= 6:  # 最多6个播放器
            messagebox.showwarning("警告", "最多只能同时播放6个流")
            return
        
        player_id = len(self.players)
        self.status_var.set(f"正在启动播放器 {player_id + 1}...")
        
        # 创建播放器窗口
        player_window = Toplevel(self.root)
        player_window.title(f"{stream_name}")
        player_window.geometry("720x480")  # 16:9比例的默认尺寸
        player_window.minsize(320, 240)    # 最小尺寸
        
        # 让窗口可以调整大小，视频会自动适应
        player_window.resizable(True, True)
        
        label = Label(player_window, text="正在加载直播流...", bg="black", fg="white", font=("Arial", 14))
        label.pack(fill=BOTH, expand=True)
        
        # 添加控制按钮
        control_frame = Frame(player_window)
        control_frame.pack(fill=X)
        Button(control_frame, text="停止播放", command=lambda: self.stop_player(player_id), bg="#ff6b6b", fg="white").pack(side=LEFT, padx=5, pady=5)
        Button(control_frame, text="重新连接", command=lambda: self.restart_player(player_id), bg="#4ecdc4", fg="white").pack(side=LEFT, padx=5, pady=5)
        
        # 添加视频信息显示
        info_label = Label(control_frame, text="", font=("Arial", 9), fg="gray")
        info_label.pack(side=RIGHT, padx=5, pady=5)
        
        player_info = {
            'window': player_window,
            'label': label,
            'info_label': info_label,
            'url': video_url,
            'name': stream_name,
            'thread': None,
            'process': None,
            'original_width': 1920,  # 默认值，会在获取到真实分辨率后更新
            'original_height': 1080
        }
        
        # 绑定窗口大小变化事件
        def on_window_resize(event=None):
            # 当窗口大小改变时，下一帧会自动按新尺寸缩放
            pass
        
        player_window.bind('<Configure>', on_window_resize)
        
        self.players.append(player_info)
        self.is_playing[player_id] = True
        
        # 更新播放列表
        self.refresh_player_list()
        
        # 启动播放线程
        self.start_player_thread(player_id)
        
        self.status_var.set(f"已启动播放器 {player_id + 1}: {stream_name}")
    
    def start_player_thread(self, player_id):
        """启动播放线程"""
        thread = threading.Thread(target=self.read_from_ffmpeg, args=(player_id,), daemon=True)
        self.players[player_id]['thread'] = thread
        thread.start()
    
    def restart_player(self, player_id):
        """重启播放器"""
        if player_id < len(self.players):
            self.is_playing[player_id] = False
            # 等待当前线程结束
            threading.Timer(1.0, lambda: self._restart_player_delayed(player_id)).start()
    
    def _restart_player_delayed(self, player_id):
        """延迟重启播放器"""
        if player_id < len(self.players):
            self.is_playing[player_id] = True
            self.start_player_thread(player_id)
    
    def stop_player(self, player_id):
        """停止指定播放器"""
        if player_id < len(self.players):
            self.is_playing[player_id] = False
            
            # 终止ffmpeg进程
            if self.players[player_id]['process']:
                try:
                    self.players[player_id]['process'].terminate()
                except:
                    pass
            
            # 关闭窗口
            try:
                self.players[player_id]['window'].destroy()
            except:
                pass
            
            # 从播放列表中移除对应项
            try:
                # 重新构建整个列表而不是删除特定索引
                self.refresh_player_list()
            except:
                pass
            
            self.status_var.set(f"已停止播放器 {player_id + 1}")
    
    def refresh_player_list(self):
        """刷新播放器列表显示"""
        self.player_listbox.delete(0, END)
        for i, player in enumerate(self.players):
            if self.is_playing.get(i, False):
                self.player_listbox.insert(END, f"播放器{i + 1}: {player['name']}")
    
    def stop_all(self):
        """停止所有播放器"""
        for i in range(len(self.players)):
            if i in self.is_playing:
                self.is_playing[i] = False
                
                # 终止ffmpeg进程
                if self.players[i]['process']:
                    try:
                        self.players[i]['process'].terminate()
                    except:
                        pass
        
        # 关闭所有窗口
        for player in self.players:
            try:
                player['window'].destroy()
            except:
                pass
        
        self.players.clear()
        self.is_playing.clear()
        self.player_listbox.delete(0, END)
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
            return 800, 600  # 默认分辨率
        except Exception:
            return 800, 600
    
    def read_from_ffmpeg(self, player_id):
        """从FFmpeg读取视频流"""
        if player_id >= len(self.players):
            return
        
        player_info = self.players[player_id]
        label = player_info['label']
        video_url = player_info['url']
        
        try:
            width, height = self.get_video_resolution(video_url)
            
            # 更新播放器信息中的原始分辨率
            self.players[player_id]['original_width'] = width
            self.players[player_id]['original_height'] = height
            
            # 根据视频比例调整窗口初始大小
            aspect_ratio = width / height
            if aspect_ratio > 1.7:  # 宽屏视频
                initial_width = 800
                initial_height = int(initial_width / aspect_ratio) + 50
            elif aspect_ratio < 1.3:  # 竖屏或接近正方形
                initial_height = 600
                initial_width = int(initial_height * aspect_ratio)
            else:  # 标准比例
                initial_width = 720
                initial_height = int(initial_width / aspect_ratio) + 50
            
            # 更新窗口大小
            self.root.after(0, lambda: player_info['window'].geometry(f"{initial_width}x{initial_height}"))
            
            # 更新视频信息显示
            info_text = f"原始: {width}x{height}"
            self.root.after(0, lambda: player_info['info_label'].config(text=info_text))
            
            command = [
                'ffmpeg',
                '-i', video_url,
                '-pix_fmt', 'rgb24',  # 直接输出RGB格式而不是BGR
                '-vcodec', 'rawvideo',
                '-an', '-sn',
                '-f', 'image2pipe', '-'
            ]
            
            pipe = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=10**8)
            self.players[player_id]['process'] = pipe
            
            frame_count = 0
            while self.is_playing.get(player_id, False):
                num_bytes = width * height * 3
                raw_image = pipe.stdout.read(num_bytes)
                
                if not raw_image:
                    break
                
                if len(raw_image) != num_bytes:
                    continue
                
                try:
                    image = np.frombuffer(raw_image, dtype='uint8').reshape((height, width, 3))
                    img = Image.fromarray(image)  # 现在FFmpeg直接输出RGB，无需转换
                    
                    # 获取播放器窗口的当前尺寸
                    try:
                        window_width = player_info['window'].winfo_width()
                        window_height = player_info['window'].winfo_height() - 50  # 减去控制按钮的高度
                        
                        # 计算保持宽高比的缩放尺寸
                        if window_width > 1 and window_height > 1:  # 确保窗口已初始化
                            # 计算缩放比例，保持原始比例
                            scale_x = window_width / width
                            scale_y = window_height / height
                            scale = min(scale_x, scale_y)  # 选择较小的缩放比例以适应窗口
                            
                            new_width = int(width * scale)
                            new_height = int(height * scale)
                            
                            # 确保尺寸不会太小
                            if new_width < 320:
                                new_width = 320
                                new_height = int(height * (320 / width))
                            if new_height < 240:
                                new_height = 240
                                new_width = int(width * (240 / height))
                                
                            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                        else:
                            # 窗口尺寸未知时，使用默认缩放但保持比例
                            target_width = 640
                            target_height = int(height * (target_width / width))
                            img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                    except:
                        # 发生错误时使用保持比例的默认尺寸
                        target_width = 640
                        target_height = int(height * (target_width / width))
                        img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                    
                    imgtk = ImageTk.PhotoImage(image=img)
                    
                    # 更新UI
                    self.root.after(0, lambda img=imgtk: self.update_image(label, img))
                    
                    frame_count += 1
                    if frame_count % 30 == 0:  # 每30帧更新一次状态
                        status_msg = f"播放中... 帧数: {frame_count}"
                        self.root.after(0, lambda msg=status_msg: self.status_var.set(msg))
                    
                except Exception as e:
                    print(f"图像处理错误: {e}")
                    continue
            
            pipe.terminate()
            
        except Exception as e:
            error_msg = f"播放错误: {str(e)}"
            print(error_msg)
            self.root.after(0, lambda msg=error_msg: label.config(text=msg))
    
    def update_image(self, label, imgtk):
        """更新图像显示"""
        try:
            label.config(image=imgtk)
            label.image = imgtk  # 保持引用
        except:
            pass  # 窗口可能已关闭
    
    # 以下是B站直播流获取的代码
    def get_real_url(self, rid):
        """获取B站直播流URL"""
        try:
            bilibili = BiliBili(rid)
            return bilibili.get_real_url()
        except Exception as e:
            raise Exception(f'获取直播流失败: {str(e)}')
    
    def run(self):
        """启动应用"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def on_closing(self):
        """窗口关闭事件"""
        self.stop_all()
        self.root.destroy()


class BiliBili:
    def __init__(self, rid):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://live.bilibili.com/',
            'Origin': 'https://live.bilibili.com'
        }
        # 先获取直播状态和真实房间号
        r_url = 'https://api.live.bilibili.com/room/v1/Room/room_init'
        param = {'id': rid}
        
        try:
            with requests.Session() as self.s:
                res = self.s.get(r_url, headers=self.header, params=param, timeout=10).json()
        except requests.exceptions.RequestException as e:
            raise Exception(f'网络连接失败: {str(e)}')
        except Exception as e:
            raise Exception(f'请求失败: {str(e)}')
            
        if 'msg' not in res or 'data' not in res:
            raise Exception(f'API返回格式错误: {res}')
            
        if res['msg'] == '直播间不存在':
            raise Exception(f'直播间 {rid} 不存在')
            
        if 'live_status' not in res['data']:
            raise Exception('无法获取直播状态')
            
        live_status = res['data']['live_status']
        if live_status != 1:
            if live_status == 0:
                raise Exception(f'直播间 {rid} 未开播')
            elif live_status == 2:
                raise Exception(f'直播间 {rid} 正在轮播')
            else:
                raise Exception(f'直播间 {rid} 状态异常 (状态码: {live_status})')
                
        self.real_room_id = res['data']['room_id']

    def get_real_url(self, current_qn: int = 10000) -> dict:
        url = 'https://api.live.bilibili.com/xlive/web-room/v2/index/getRoomPlayInfo'
        param = {
            'room_id': self.real_room_id,
            'protocol': '0,1',
            'format': '0,1,2',
            'codec': '0,1',
            'qn': current_qn,
            'platform': 'h5',
            'ptype': 8,
        }
        
        try:
            with requests.Session() as s:
                s.headers.update(self.header)
                res = s.get(url, params=param, timeout=15).json()
        except requests.exceptions.RequestException as e:
            raise Exception(f'获取播放信息网络错误: {str(e)}')
        except Exception as e:
            raise Exception(f'获取播放信息失败: {str(e)}')
        
        if 'data' not in res:
            raise Exception(f'播放API返回错误: {res}')
        
        playurl_info = res['data'].get('playurl_info')
        if not playurl_info:
            raise Exception('无法获取播放信息，直播可能已结束')
        
        playurl = playurl_info.get('playurl')
        if not playurl:
            raise Exception('无法获取播放URL信息')
        
        stream_info = playurl.get('stream', [])
        if not stream_info:
            raise Exception('无法获取流信息，直播源可能不可用')

        stream_urls = {}
        
        # 优先获取FLV格式
        for data in stream_info:
            if 'format' not in data:
                continue
                
            for format_data in data['format']:
                format_name = format_data.get('format_name', '')
                if format_name == 'flv':
                    if 'codec' in format_data and format_data['codec']:
                        codec_data = format_data['codec'][0]
                        base_url = codec_data.get('base_url', '')
                        url_info = codec_data.get('url_info', [])
                        
                        for i, info in enumerate(url_info):
                            host = info.get('host', '')
                            extra = info.get('extra', '')
                            if host and base_url:
                                complete_url = f'{host}{base_url}{extra}'
                                stream_urls[f'FLV线路{i + 1}'] = complete_url
                    break
            
            if stream_urls:
                break
        
        # 如果没有FLV，获取HLS
        if not stream_urls:
            for data in stream_info:
                if 'format' not in data:
                    continue
                    
                for format_data in data['format']:
                    format_name = format_data.get('format_name', '')
                    if format_name == 'ts':
                        if 'codec' in format_data and format_data['codec']:
                            codec_data = format_data['codec'][0]
                            base_url = codec_data.get('base_url', '')
                            url_info = codec_data.get('url_info', [])
                            
                            for i, info in enumerate(url_info):
                                host = info.get('host', '')
                                extra = info.get('extra', '')
                                if host and base_url:
                                    complete_url = f'{host}{base_url}{extra}'
                                    stream_urls[f'HLS线路{i + 1}'] = complete_url
                        break
                
                if stream_urls:
                    break
        
        if not stream_urls:
            raise Exception('未找到可用的直播流地址，可能是网络问题或直播源不可用')
            
        return stream_urls


if __name__ == "__main__":
    # 检查ffmpeg
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except:
        print("错误: 未找到ffmpeg，请确保已安装ffmpeg并添加到PATH")
        sys.exit(1)
    
    app = BiliBiliLivePlayer()
    app.run()
