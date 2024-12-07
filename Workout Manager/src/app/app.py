from PyQt6.QtWidgets import QApplication

class Application(QApplication):
    """
    Creates the application for the UI to run in.
    """

    def __init__(self, argv:list[str]):
        """
        Creates and initializes an Application object.

        Args:
            argv (list[str]): command-line arguments
        """
        super().__init__(argv)