import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.can_Sphere = False
        self.evx = 0
        self.evy = 0
        self.pushButton.clicked.connect(self.flag)

    def flag(self):
        self.can_Sphere = True
        self.repaint()

    def paintEvent(self, event):
        if self.can_Sphere:
            qp = QPainter()
            qp.begin(self)
            self.draw_sphere(qp)
            qp.end()

    def draw_sphere(self, qp):
        for i in range(random.randint(0, 20)):
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500))
            self.can_Sphere = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())