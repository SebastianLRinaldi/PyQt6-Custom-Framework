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
"""
Test this see if anything changes in terms of speed?
"""
# os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--use-gl=angle --gpu --gpu-launcher --in-process-gpu --ignore-gpu-blacklist --ignore-gpu-blocklist'

# Add the root directory of your project to the sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# from application.FrontEnd.presentations.mySecondWindow.mySecondWindowLayout import *
# from application.FrontEnd.presentations.myFirstWindow.myFirstWindowLayout import *

# # ----- App Modules -----
# class MusicApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         layout.addWidget(QPushButton("Play Music"))
#         self.setLayout(layout)

# class MapsApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         layout.addWidget(QPushButton("Open Map"))
#         self.setLayout(layout)


# class Dashboard(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Car UI")
#         self.resize(800, 480)

#         self.stack = QStackedWidget()
#         self.apps = {
#             "music": MusicApp(),
#             "maps": MapsApp(),
#         }

#         for app in self.apps.values():
#             self.stack.addWidget(app)

#         # Nav buttons
#         nav = QHBoxLayout()
#         for name in self.apps:
#             btn = QPushButton(name.capitalize())
#             btn.clicked.connect(lambda _, n=name: self.switch_to(n))
#             nav.addWidget(btn)

#         container = QWidget()
#         layout = QVBoxLayout(container)
#         layout.addLayout(nav)
#         layout.addWidget(self.stack)

#         self.setCentralWidget(container)
#         self.switch_to("music")

#     def switch_to(self, app_name):
#         self.stack.setCurrentWidget(self.apps[app_name])

# # ----- Entry Point -----
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = Dashboard()
#     win.show()
#     sys.exit(app.exec())


# from application.FrontEnd.presentations.myFirstWindow.myFirstWindowLayout import My_First_Page
# from application.FrontEnd.presentations.myThirdWindow.myThirdWindowLayout import My_Third_Page
# from PyQt6.QtWidgets import QLabel, QPushButton, QWidget, QVBoxLayout
# from typing import Dict, TypedDict

# Assuming you are using PyQt6 and these are your actual UI class types
# class My_First_Page(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.label: QLabel = QLabel("First Page Label", self)
#         self.update_widget_btn: QPushButton = QPushButton("Update", self)
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.label)
#         layout.addWidget(self.update_widget_btn)

# class My_Third_Page(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.label: QLabel = QLabel("Third Page Label", self)
#         self.update_widget_btn: QPushButton = QPushButton("Update", self)
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.label)
#         layout.addWidget(self.update_widget_btn)

# Define your logic classes
# class FirstPageLogic:
#     def __init__(self, ui: My_First_Page):
#         self.ui: My_First_Page = ui

# class SecondPageLogic:
#     def __init__(self, ui: My_Third_Page):
#         self.ui: My_Third_Page = ui

#     def update_label(self, text: str):
#         self.ui.label.setText(text)

# # This is your scalable logic dict
# class LogicDict(TypedDict):
#     first: FirstPageLogic
#     second: SecondPageLogic
#     # Add more entries here for new pages as needed


# # Page Controller can now scale without problems
# class PageController:
#     def __init__(self, logic: LogicDict):
#         self.logic = logic
#         self.connect_signals()

#     def connect_signals(self):
#         # Dynamically connects first page's signal to second page's method
#         self.logic["first"].ui.update_widget_btn.clicked.connect(
#             lambda: self.logic["second"].update_label("Updated from First Page")
#         )

from application.FrontEnd.E_combiner.PageController import *
from application.apps.myFirstWindow.myFirstWindowConnections import FirstPageConnections
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











# def main():
#     app = QApplication(sys.argv)
#     my_first_page()
#     my_second_page()
    
#     return app.exec()  
    
# if __name__ == "__main__":
#     main()
