from .view import Window
from PyQt5.QtWidgets import QApplication
import sys
from .database import createConnection

def main():
    app = QApplication(sys.argv)
    if not createConnection("POS.sqlite"):
        sys.exit(1)
    win = Window()
    win.show()
    sys.exit(app.exec_())