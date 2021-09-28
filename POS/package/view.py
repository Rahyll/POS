import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import POS.qrc_resources

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
    QLineEdit,
    QFormLayout,
    QVBoxLayout,
    QDialog,

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
        self.new = QAction("&New", self)
        menubar.addMenu('&Tools').addAction(self.new)
        opendialog=AddDialog()
        self.new.triggered.connect(opendialog.exec())
    def _createToolBar(self):
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)
        toolbar.addAction(QIcon(":plus.svg"),"&Add")
        toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        toolbar.setMovable(False)



class AddDialog(QDialog):
    """Add dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def setupUI(self):
        self.name = QLineEdit()
        self.Quantity = QLineEdit()
        layout = QFormLayout()
        layout.addRow("Name",self.name)
        layout.addRow("Amount",self.Quantity)
        self.layout.addLayout(layout)



