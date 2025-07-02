import pyautogui, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import QTimer, Qt


# print('Press Ctrl-C to quit')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x) + '\n' + 'Y:' + str(y)
#         print(positionStr)
#         # print(len(positionStr))
#         sleep(1)
# except KeyboardInterrupt:
#     print('\n')

# x, y = pyautogui.position()
# positionStr = 'X: ' + str(x) + 'Y:' + str(y)
# print(positionStr)
# print(len(positionStr))


class WinForm(QWidget):
    def __init__(self, parent = None):
        super(WinForm, self).__init__(parent)
        self.status = ""
        self.timer = QTimer(self)
        self.setFixedSize(360, 100)
        self.setWindowTitle('current mouse position')
        self.File = QLabel()

        x, y = pyautogui.position()
        self.File.setText('X: ' + str(x) + '\n' + 'Y:' + str(y))
        self.File.setFont(QFont('Arial', 15))

        # palette_white = QPalette()
        # palette_white.setColor(QPalette.Window, Qt.red)
        # self.File.setPalette(palette_white)
        self.File.setAlignment(Qt.AlignCenter)
    
        layout = QGridLayout(self)
        layout.addWidget(self.File, 0, 0, 1, 1)

        self.setLayout(layout)

        self.timer.timeout.connect(self.check)
        self.timer.start(1)

    def check(self):
        x, y = pyautogui.position()
        self.File.setText('X: ' + str(x) + '\n' + 'Y:' + str(y))
        QApplication.processEvents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())