import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyAppTest(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('C:\\Users\\admin\\Downloads\\IMG_0013.PNG'))
        self.setGeometry(300,300,3000,2000)
        self.show()
    
if __name__ == '__main__':
    app = QApplication (sys.argv)
    ex = MyAppTest()
    sys.exit(app.exec_())
