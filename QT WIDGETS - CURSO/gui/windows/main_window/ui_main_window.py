#IMPORT QT CORE
from qt_core import *   

# MAIN WINDOW
class Ui_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")


        # SET INITIAL PARAMETERS
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)
        parent.setMaximumSize(1200, 720)


        # SET CENTRAL WIDGET
        self.central_frame = QFrame()


        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame) #QH -> Horizontal Layout
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        #LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        
        # CONTENT 
        self.content = QFrame()
        self.content.setStyleSheet("Background-Color: #282a36")

        # ADD WIDGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)


        parent.setCentralWidget(self.central_frame) 