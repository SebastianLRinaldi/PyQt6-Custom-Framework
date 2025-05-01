import sys
import ctypes

import win32gui
import win32con
import subprocess
import time

import os
import sys
import time
import re

import threading
from threading import Thread
from enum import Enum
from queue import Queue
from typing import List
from datetime import timedelta

from PyQt6.QtCore import Qt
from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
# from PyQt6.QtWebEngineWidgets import QWebEngineView
from application.FrontEnd.A_frameworks.widgetFrameworks import ConnectedWidget, IsolatedWidget


# class WebPage(QWebEngineView, IsolatedWidget):
#     def __init__(self, url="https://example.com", widgetRow=-1, widgetCol=-1, widgetRowSpan=-1, widgetColSpan=-1, *args, **kwargs):
#         IsolatedWidget.__init__(self, widgetRow, widgetCol, widgetRowSpan, widgetColSpan, *args, **kwargs)
#         QWebEngineView.__init__(self, *args, **kwargs)
#         self.setUrl(QUrl(url))

#     def load_url(self, url):
#         self.setUrl(QUrl(url))

class EmbeddedWebPage(IsolatedWidget):
    def __init__(self, widgetRow=-1, widgetCol=-1, widgetRowSpan=-1, widgetColSpan=-1, parent=None, *args, **kwargs):
        IsolatedWidget.__init__(self, widgetRow, widgetCol, widgetRowSpan, widgetColSpan, *args, **kwargs)
        self.setLayout(QVBoxLayout())

        self.no_window_label = QLabel("NO WINDOW")
        # self.no_window_label.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(self.no_window_label)

        self.hwnd = None

    def embed_window(self, hwnd):
        if hwnd:
            self.no_window_label.hide()
            win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, win32con.WS_VISIBLE | win32con.WS_CHILD)
            ctypes.windll.user32.SetParent(hwnd, int(self.winId()))
            win32gui.MoveWindow(hwnd, 0, 0, self.width(), self.height(), True)
            self.hwnd = hwnd
        else:
            self.hwnd = None
            self.no_window_label.show()

    def resizeEvent(self, event):
        if self.hwnd:
            win32gui.MoveWindow(self.hwnd, 0, 0, self.width(), self.height(), True)
        super().resizeEvent(event)



# class EmbeddedApp(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setLayout(QVBoxLayout())

#     def embed_window(self, hwnd):
#         # Change the style of the external window to be a child window
#         win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, win32con.WS_VISIBLE | win32con.WS_CHILD)
#         # Reparent the external window into this widget
#         ctypes.windll.user32.SetParent(hwnd, int(self.winId()))
#         # Resize the external window to fit this widget
#         win32gui.MoveWindow(hwnd, 0, 0, self.width(), self.height(), True)

#     def resizeEvent(self, event):
#         # Adjust external window size when this widget is resized
#         if hasattr(self, 'hwnd') and self.hwnd:
#             win32gui.MoveWindow(self.hwnd, 0, 0, self.width(), self.height(), True)
#         super().resizeEvent(event)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Embed Windows Settings")
#         self.resize(800, 600)

#         # Main layout
#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)
#         self.layout = QVBoxLayout(self.central_widget)

#         # Button to open Windows Settings
#         self.settings_button = QPushButton("Open Windows Settings", self)
#         self.settings_button.clicked.connect(self.open_windows_settings)
#         self.layout.addWidget(self.settings_button)

#         # Embedded application container
#         self.embedded_app = EmbeddedApp(self)
#         self.layout.addWidget(self.embedded_app)

#     def open_windows_settings(self):
#         # Launch the Windows Settings app
#         # subprocess.run(["start", "ms-settings:"], shell=True)
#         time.sleep(2)  # Wait for the window to open

#         # Find the window handle of the settings app
#         # hwnd = win32gui.FindWindow(None, "My Webview")  # Update with the correct window title if necessary
#         hwnd = win32gui.FindWindow(None, "Speed Dial - Opera")
#         if hwnd:
#             self.embedded_app.hwnd = hwnd
#             self.embedded_app.embed_window(hwnd)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
