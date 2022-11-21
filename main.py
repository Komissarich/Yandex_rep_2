import sys
import random as rd
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget
from PyQt5 import uic
SCREEN_SIZE = [400, 400]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()


    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        a = rd.randint(50, 500)
        c = rd.randint(50, 500)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(a, a, c, c)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())