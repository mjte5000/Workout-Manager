"""
Module that creates the main window for the application.
"""
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class MainWindow(QMainWindow):
    """
    Creates the main window for the application.
    """

    def __init__(self, parent:QWidget):
        """
        Creates and initializes a MainWindow object.

        Args:
            parent (QWidget): the parent widget of this widget.
        """
        super().__init__(parent)

        self.setWindowTitle("Workout Manager")
        
        # Menu bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Menu bar > File
        self.file_menu = QMenu("File", self)
        self.menu_bar.addMenu(self.file_menu)

        # Menu bar > File > New log
        self.new_log = QAction("Create new log...", self)
        self.file_menu.addAction(self.new_log)

        # Menu bar > File > Load log
        self.load_log = QAction("Load log from file...", self)
        self.file_menu.addAction(self.load_log)

        # Menu bar > File > Save log
        self.save_log = QAction("Save log to file...", self)
        self.file_menu.addAction(self.save_log)

        # Central widget
        self.central_widget = CentralWidget(self)
        self.setCentralWidget(self.central_widget)

class CentralWidget(QWidget):
    """
    Creates the central widget for the main window.
    """

    def __init__(self, parent:MainWindow):
        """
        Creates and initializes a CentralWidget object.

        Args:
            parent (MainWindow): the main window this widget will be contained
                in
        """
        super().__init__(parent)