from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Workout Manager")
        
        # Menu bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Menu bar > Tools
        self.tools_menu = QMenu("Tools", self.menu_bar)
        self.menu_bar.addMenu(self.tools_menu)

        # Menu bar > Tools > Query
        self.query_action = QAction("Query", self.tools_menu)
        self.tools_menu.addAction(self.query_action)
