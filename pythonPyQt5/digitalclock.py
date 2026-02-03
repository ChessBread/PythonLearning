import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class Dig_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital clock")
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 150px;"
                                      "font-family: Arial;"
                                      "color: blue")

        self.setStyleSheet("background-color: black;")

        # ✅ ADD THESE LINES
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # update every second
        self.update_time()      # show time immediately

    def update_time(self):
        currennt_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(currennt_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Dig_clock()
    clock.show()
    sys.exit(app.exec_())
