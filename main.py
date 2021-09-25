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
        def _createmenuBar(self):
            menubar=QMenuBar(self)
            self.setMenuBar(menubar)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


    
    