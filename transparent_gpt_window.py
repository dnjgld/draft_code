import openai
import pyperclip
import tkinter as tk
import threading

# setup OpenAI API key
openai.api_key = ""

# ChatGPT的搜索函数
def chatgpt_search(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            # model = "gpt-3.5-turbo",
            messages=[
                {"role":"system","content":"You are a helpful assitant"},
                {"role":"user","content":query},
            ]
        )
        print(response['choices'][0]['message']['content'])
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)

# 创建一个透明的Tkinter窗口
root = tk.Tk()
root.attributes("-alpha", 1)  # 设置透明度（0表示完全透明，1表示不透明）
# root.attributes("-alpha", 1)  # 设置透明度（0表示完全透明，1表示不透明）

# 创建一个文本框用于显示搜索结果
result_text = tk.Text(root, height=10, width=40)

font = ("Helvetica", 16)
result_text.config(font=font)
#
scrollbar = tk.Scrollbar(root, command=result_text.yview)
result_text.config(yscrollcommand=scrollbar.set)

result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# def on_enter(event): 
#     root.attributes("-alpha", 0.00) 
#     # 进入窗口时设置完全不透明 
#     # 鼠标离开窗口时还原透明度 
#     result_text.delete(1.0, tk.END)
# def on_leave(event): 
#     root.attributes("-alpha", 0.05) 
# # 离开窗口时还原透明度 # 绑定鼠标事件 

# root.bind("<Enter>", on_enter) 
# root.bind("<Leave>", on_leave)

def toggle_transparency(event):
    global is_transparent
    if is_transparent:
        root.attributes("-alpha", 1)  # 切换为完全不透明
        is_transparent = False
    else:
        root.attributes("-alpha", 0.01)  # 切换为透明
        is_transparent = True

is_transparent = False
root.bind("<Button-1>", toggle_transparency)

# 监听剪贴板变化的线程
def clipboard_monitor():
    previous_clipboard_text = pyperclip.paste()
    while True:
        current_clipboard_text = pyperclip.paste()
        if current_clipboard_text != previous_clipboard_text:
            print(current_clipboard_text)
            result_text.delete(1.0, tk.END)  # 清空文本框
            # result_text.insert(tk.END, f"问题：\n{current_clipboard_text}\n...\n")
            previous_clipboard_text = current_clipboard_text
            search_query = current_clipboard_text.strip()
            if search_query:
                result = chatgpt_search(search_query)
                result_text.insert(tk.END, f"搜索结果：\n{result}")

# 启动剪贴板监视线程
clipboard_thread = threading.Thread(target=clipboard_monitor)
clipboard_thread.daemon = True
clipboard_thread.start()

# 启动Tkinter主循环
root.mainloop()




