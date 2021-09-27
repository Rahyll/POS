from .view import Window
from PyQt5.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())