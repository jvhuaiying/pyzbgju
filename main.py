import sys
from Class0 import NetworkCard
from Class1 import MainWindow1
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QGuiApplication
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, \
    QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.NetworkCard = None
        self.BPF = None
        self.setWindowTitle("抓包程序")
        self.setFixedSize(600, 400)
        # 窗口置顶
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.data0 = None
        self.button0_0 = None
        self.combox0_0 = None
        self.button0_1 = None
        self.combox0_1 = None
        self.input0_0 = None
        self.layout1_1 = None
        self.title0_0 = None
        self.input0_1 = None
        self.layout0_0 = None
        self.layout1_0 = None
        self.center()
        self.layout0()
        self.layout1()
        self.title0()
        self.input0()
        self.combox0()
        self.button0()

    def center(self):
        screen = QGuiApplication.primaryScreen().size()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))

    def layout0(self):
        self.layout0_0 = QVBoxLayout()
        self.widget.setLayout(self.layout0_0)

    def layout1(self):
        self.layout1_0 = QHBoxLayout()
        self.layout1_1 = QHBoxLayout()
        self.layout1_2 = QHBoxLayout()
        self.layout1_3 = QHBoxLayout()
        self.layout0_0.addStretch()
        self.layout0_0.addLayout(self.layout1_0)
        self.layout0_0.addStretch()
        self.layout0_0.addLayout(self.layout1_1)
        self.layout0_0.addStretch()
        self.layout0_0.addLayout(self.layout1_2)
        self.layout0_0.addStretch()
        self.layout0_0.addLayout(self.layout1_3)
        self.layout0_0.addStretch()

    def title0(self):
        self.title0_0 = QLabel("欢迎使用抓包程序")
        self.title0_0.setFont(QFont("楷体", 24, QFont.Weight.Bold))
        self.title0_0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout1_0.addWidget(self.title0_0)

    # input box
    def input0(self):
        self.input0_0 = QLabel("BPF过滤器：")
        self.input0_0.setFont(QFont("Microsoft YaHei", 14, QFont.Weight.Normal))
        self.input0_0.setFixedWidth(110)
        self.input0_1 = QLineEdit()
        self.input0_1.setFixedWidth(300)
        self.input0_1.setFont(QFont("Microsoft YaHei", 14, QFont.Weight.Normal))
        self.layout1_1.addStretch()
        self.layout1_1.addWidget(self.input0_0)
        self.layout1_1.addWidget(self.input0_1)
        self.layout1_1.addStretch()

    def combox0(self):
        self.data0 = NetworkCard().data()
        self.combox0_0 = QLabel("网卡选择：")
        self.combox0_0.setFont(QFont("Microsoft YaHei", 14, QFont.Weight.Normal))
        self.combox0_0.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.combox0_0.setFixedWidth(110)
        self.combox0_1 = QComboBox()
        self.combox0_1.addItems(self.data0)
        self.combox0_1.setFont(QFont("Microsoft YaHei", 14, QFont.Weight.Normal))
        self.combox0_1.setFixedWidth(300)
        self.layout1_2.addStretch()
        self.layout1_2.addWidget(self.combox0_0)
        self.layout1_2.addWidget(self.combox0_1)
        self.layout1_2.addStretch()

    def button0(self):
        self.button0_0 = QPushButton("开始抓包")
        self.button0_0.setFont(QFont("Microsoft YaHei", 12, QFont.Weight.Normal))
        self.button0_0.setFixedWidth(140)
        self.button0_0.setFixedHeight(40)
        self.button0_0.setCursor(Qt.CursorShape.PointingHandCursor)
        self.button0_0.clicked.connect(self.button0_0_clicked)
        self.button0_1 = QPushButton("退出应用")
        self.button0_1.setFont(QFont("Microsoft YaHei", 12, QFont.Weight.Normal))
        self.button0_1.setFixedWidth(140)
        self.button0_1.setFixedHeight(40)
        self.layout1_3.addStretch()
        self.layout1_3.addWidget(self.button0_0)
        self.layout1_3.addStretch()
        self.layout1_3.addWidget(self.button0_1)
        self.layout1_3.addStretch()

    def button0_0_clicked(self):
        if self.input0_1.text() == "":
            QMessageBox.information(self, "提示", "请输入BPF过滤器")
        else:
            self.BPF = self.input0_1.text()
            self.NetworkCard = self.combox0_1.currentText()
            self.close()
            self.window = MainWindow1(self.NetworkCard, self.BPF)
            self.window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
