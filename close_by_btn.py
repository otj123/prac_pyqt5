import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class MA(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("닫기",self)
        btn.move(50,50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('종료버튼')
        self.setGeometry(300,300, 500,400)
        self.show()
if __name__ == '__main__':
    print('test')
    print(sys.argv)
    app = QApplication(sys.argv)
    ex = MA()
    sys.exit(app.exec_())
    
    