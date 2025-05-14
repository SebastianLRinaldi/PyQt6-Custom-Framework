"""
pyqt6 - v. 6.7 (G) || 6.9 (G)
pyqt6-webengine - v. 6.7 (G)
"""
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtPrintSupport import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWebEngineCore import *
import sys
import os

# os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--use-gl=angle --gpu --gpu-launcher --in-process-gpu --ignore-gpu-blacklist --ignore-gpu-blocklist'

# Add the root directory of your project to the sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from application.FrontEnd.E_combiner.PageController import *
from application.apps.myFirstWindow.myFirstWindowConnections import FirstPageConnections
from application.apps.mySecondWindow.mySecondWindowConnections import SecondPageConnections
from application.apps.myThirdWindow.myThirdPageConnections import ThirdPageConnections

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Car UI")
        self.resize(800, 480)

        self.stack = QStackedWidget()

        # Your dynamic page creation
        # Define pages with: name, UI class, Logic class, Controller class
        pages = [
            ("first", My_First_Page, FirstPageLogic, FirstPageConnections),
            ("second", My_Second_Page, SecondPageLogic, SecondPageConnections),
            ("third", My_Third_Page, ThirdPageLogic, ThirdPageConnections),
        ]

        # Step 1: Create UIs
        self.apps = {name: page_class() for name, page_class, *_ in pages}

        # Step 2: Create Logic
        self.logic = {name: logic_class(self.apps[name]) for name, _, logic_class, _ in pages}

        # Step 3: Create Per-Page Controllers
        self.page_controllers = {
            name: controller_class(self.apps[name], self.logic[name])
            for name, _, _, controller_class in pages
        }

        # Add pages to the stack
        for page in self.apps.values():
            self.stack.addWidget(page)

        # Create the controller
        self.controller = PageController(self.logic)

        
        # Nav buttons
        nav = QHBoxLayout()
        for name in self.apps:
            btn = QPushButton(name.capitalize())
            btn.clicked.connect(lambda _, n=name: self.switch_to(n))
            nav.addWidget(btn)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addLayout(nav)
        layout.addWidget(self.stack)

        self.setCentralWidget(container)
        self.switch_to("first")

    def switch_to(self, app_name):
        self.stack.setCurrentWidget(self.apps[app_name])


# ----- Entry Point -----
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dashboard()
    win.show()
    sys.exit(app.exec())
