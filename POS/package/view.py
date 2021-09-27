import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from PyQt5.QtWidgets import (

    QApplication,

    QMainWindow,

    QMessageBox,

    QTableWidget,

    QTableWidgetItem,
    QWidget,
    QMenuBar

)
class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("POS")
        self.resize(800, 600)
        self.widget=QWidget()
        self.setCentralWidget(self.widget)
