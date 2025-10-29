import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor, QPalette

# 20条不同的语句
messages = [
    "早安，开启美好一天！",
    "天冷了，多穿衣服",
    "不顺心的话就找我叭",
    "多喝水哦~",
    "要天天开心吖~",
    "保持好心情",
    "照顾好自己",
    "别熬夜",
    "早点休息",
    "今天过的开心嘛",
    "今天也要加油哦！",
    "梦想成真",
    "保持微笑吖",
    "愿你所有烦恼都消失",
    "多吃水果",
    "要按时吃饭",
    "你值得被世界温柔以待",
    "好好爱自己",
    "顺顺利利",
    "愿你笑容常在。"
]

# 淡暖色调列表（RGB）
warm_colors = [
    (255, 239, 213),  # 浅橙
    (255, 228, 196),  # 浅米
    (255, 222, 173),  # 浅黄
    (255, 182, 193),  # 浅粉
    (255, 204, 153),  # 浅橙黄
    (255, 250, 205),  # 柠檬黄
    (255, 245, 238),  # 雪白暖色
    (255, 228, 225),  # 薄雾玫瑰
    (255, 218, 185),  # 桃色
    (255, 160, 122),  # 浅珊瑚
    (255, 236, 139),  # 浅金黄
    (255, 215, 180),  # 浅杏色
    (255, 223, 211),  # 浅橙粉
    (255, 240, 245),  # 浅紫粉
    (255, 250, 240),  # 浅米白
    (255, 239, 213),  # 浅橙
    (255, 228, 181),  # 浅黄棕
    (255, 192, 203),  # 粉色
    (255, 228, 225)   # 薄雾玫瑰
]

class Popup(QWidget):
    def __init__(self, message, color):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool)
        # 1080P
        # self.setFixedSize(180, 40)
        # 2K
        self.setFixedSize(200, 60)
        self.setWindowTitle("⚠️温馨提示")
        label = QLabel(message, self)
        label.setStyleSheet("font-size: 20px; font-weight: bold; color: #333; font-family: 微软雅黑;")
        label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(*color))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

class PopupGenerator:
    def __init__(self):
        self.count = 0
        self.max_count = 300    # 数量
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_popup)
        self.timer.start(20)    # 速度

    def show_popup(self):
        if self.count < self.max_count:
            msg = messages[self.count%messages.__len__()]
            color = warm_colors[self.count%warm_colors.__len__()]
            popup = Popup(msg, color)
            # 随机位置
            # 1080P
            # x = random.randint(20, 1900)
            # y = random.randint(20, 1000)
            # 2K
            x = random.randint(20, 2500)
            y = random.randint(20, 1600)
            popup.move(x, y)
            popup.show()
            # 保持弹窗引用，防止被垃圾回收
            QApplication.instance().activePopups.append(popup)
            self.count += 1
        else:
            self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.activePopups = []
    generator = PopupGenerator()
    sys.exit(app.exec_())