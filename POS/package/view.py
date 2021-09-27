import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from PyQt5.QtWidgets import (

    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
    QMenuBar,
    QAction,
    QToolBar,

)
class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("POS")
        self.resize(800, 600)
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self._createMenuBar()
        self._createToolBar()

    def _createMenuBar(self):
        menubar=QMenuBar(self)
        self.setMenuBar(menubar)
        new = QAction("&New", self)
        menubar.addMenu('&Tools').addAction(new)
    def _createToolBar(self):
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)

