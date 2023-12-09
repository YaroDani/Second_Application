from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton
app=QApplication([])
main_win=QWidget()
main_win.resize(400,200)
main_win.setWindowTitle("Конкурс від Crazy People")

question=QLabel("В якому році канал отримав Золоту кнопку від YouTube?")
btn1=QRadioButton("2005")
btn2=QRadioButton("2010")
btn3=QRadioButton("2015")
btn4=QRadioButton("2020")

layout_main=QVBoxLayout()
layoutH1=QHBoxLayout()
layoutH2=QHBoxLayout()
layoutH3=QHBoxLayout()

layoutH1.addWidget(question,alignment=Qt.AlignCenter)
layoutH2.addWidget(btn1,alignment=Qt.AlignCenter)
layoutH2.addWidget(btn2,alignment=Qt.AlignCenter)
layoutH3.addWidget(btn3,alignment=Qt.AlignCenter)
layoutH3.addWidget(btn4,alignment=Qt.AlignCenter)
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)
def show_win():
    victory=QMessageBox()
    victory.setText("Правильно! Ви виграли гіроскутер")
    victory.exec_()
def show_lose():
    lose=QMessageBox()
    lose.setText("Ні, в 2005 році. Ви виграли фірмовий плакат")
    lose.exec_()

btn1.clicked.connect(show_win)
btn2.clicked.connect(show_lose)
btn3.clicked.connect(show_lose)
btn4.clicked.connect(show_lose)
main_win.show()
app.exec_()