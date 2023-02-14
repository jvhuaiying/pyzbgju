from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QGuiApplication
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, \
    QAbstractItemView, QPushButton, QTextEdit


class MainWindow1(QMainWindow):
    def __init__(self, networkCard, bpf):
        super().__init__()
        self.layout1_3 = None
        self.button0_0 = None
        self.button0_1 = None
        self.button0_2 = None
        self.button0_3 = None
        self.button0_4 = None
        self.table0_0 = None
        self.layout0_0 = None
        self.layout1_0 = None
        self.layout1_1 = None
        self.layout1_2 = None
        self.NetworkCard = networkCard
        self.BPF = bpf
        self.setWindowTitle("开始抓包")
        self.setFixedSize(1800, 600)
        # 窗口置顶
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.center()
        self.layout0()
        self.layout1()
        self.button0()
        self.table0()
        self.table1()
        self.textEdit0()

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

    def button0(self):
        button_width = 150
        self.button0_0 = QPushButton("开始")
        self.button0_0.setFixedSize(button_width, 30)
        self.button0_0.setFont(QFont("Microsoft YaHei", 10, QFont.Weight.Normal))
        self.button0_1 = QPushButton("暂停")
        self.button0_1.setFixedSize(button_width, 30)
        self.button0_1.setFont(QFont("Microsoft YaHei", 10, QFont.Weight.Normal))
        self.button0_2 = QPushButton("停止")
        self.button0_2.setFixedSize(button_width, 30)
        self.button0_2.setFont(QFont("Microsoft YaHei", 10, QFont.Weight.Normal))
        self.button0_3 = QPushButton("保存")
        self.button0_3.setFixedSize(button_width, 30)
        self.button0_3.setFont(QFont("Microsoft YaHei", 10, QFont.Weight.Normal))
        self.button0_4 = QPushButton("退出")
        self.button0_4.setFixedSize(button_width, 30)
        self.button0_4.setFont(QFont("Microsoft YaHei", 10, QFont.Weight.Normal))
        self.layout1_0.addStretch()
        self.layout1_0.addWidget(self.button0_0)
        self.layout1_0.addStretch()
        self.layout1_0.addWidget(self.button0_1)
        self.layout1_0.addStretch()
        self.layout1_0.addWidget(self.button0_2)
        self.layout1_0.addStretch()
        self.layout1_0.addWidget(self.button0_3)
        self.layout1_0.addStretch()
        self.layout1_0.addWidget(self.button0_4)
        self.layout1_0.addStretch()

    def table0(self):
        self.table0_0 = QTableWidget()
        self.table0_0.setColumnCount(7)
        self.table0_0.setRowCount(0)
        self.table0_0.setHorizontalHeaderLabels(["No.", "Time", "Source", "Destination", "Protocol", "Length", "Info"])
        # self.table0_0.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table0_0.verticalHeader().setVisible(False)
        self.table0_0.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table0_0.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table0_0.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table0_0.setAlternatingRowColors(True)
        self.table0_0.setColumnWidth(0, 100)
        self.table0_0.setColumnWidth(1, 180)
        self.table0_0.setColumnWidth(2, 160)
        self.table0_0.setColumnWidth(3, 160)
        self.table0_0.setColumnWidth(4, 100)
        self.table0_0.setColumnWidth(5, 100)
        self.table0_0.setColumnWidth(6, 800)
        self.layout1_1.addWidget(self.table0_0)

    def table1(self):
        self.table0_0 = QTableWidget()
        self.table0_0.setColumnCount(1)
        self.table0_0.setRowCount(0)
        self.table0_0.setHorizontalHeaderLabels(["packet dissection"])
        self.table0_0.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table0_0.verticalHeader().setVisible(False)
        self.table0_0.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table0_0.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table0_0.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table0_0.setAlternatingRowColors(True)
        self.layout1_2.addWidget(self.table0_0)

    def textEdit0(self):
        self.textEdit0_0 = QTextEdit()
        self.layout1_3.addWidget(self.textEdit0_0)
