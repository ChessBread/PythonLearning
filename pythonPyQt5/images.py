import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon

class  MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700,300, 600, 600)
        

        label  = QLabel(self)
        label.setGeometry(0, 0, 300, 300)



        pixmap = QPixmap("/home/aldie/Documents/alden_python/pythonPyQt5/1116544.png")
        label.setPixmap(pixmap)


        label.setScaledContents(True)



        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()