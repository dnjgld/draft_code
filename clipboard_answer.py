import win32clipboard
from PIL import Image, ImageGrab
import pyperclip
def get_clipboard_content():
    """
    获取剪贴板内容。如果是文本，返回文本。如果是图像，返回图像。
    """
    # 打开剪贴板
    win32clipboard.OpenClipboard()
    try:
        # 尝试获取剪贴板的文本
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
            raw_data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
            
            try:
                text = raw_data.decode('utf-8')
            except UnicodeDecodeError:
                try:
                    text = raw_data.decode('cp1252')
                except:
                    text = raw_data.decode('utf-8', errors='replace')

            return ("text", text)
            # print(text)

        # 尝试获取剪贴板的图像
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_DIB):
            img = ImageGrab.grabclipboard()
            return ("image", img)

    finally:
        try:
            win32clipboard.CloseClipboard()
        except:
            pass

    return None

content = get_clipboard_content()

if content:
    if content[0] == "text":
        print("Text from clipboard:", content[1])
    elif content[0] == "image":
        content[1].show()
else:
    print("Clipboard is empty or format not recognized.")
