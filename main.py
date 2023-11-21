import sys
import random
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow


class DrawYellowCircle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.is_drawing = False
        self.push_btn.clicked.connect(self.result)

    def paintEvent(self, event):
        if self.is_drawing:
            painter = QPainter(self)
            for _ in range(3):
                brush = QBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                painter.setBrush(brush)
                side = random.randint(20, 50)
                x = random.randint(0, 800)
                y = random.randint(0, 600)
                painter.drawEllipse(x - side, y - side, side * 2, side * 2)
                self.is_drawing = False

    def result(self):
        self.is_drawing = True
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawYellowCircle()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
