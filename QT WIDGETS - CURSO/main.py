# IMPORT MODULES
import sys
import os

# IMPORT QT CORE
from qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import Ui_MainWindow

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # CHAMA METDO DE CONFIGURAÇÃO INICIAL
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)

        # EXIBE A APLICAÇÃO
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())