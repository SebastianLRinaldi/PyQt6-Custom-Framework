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

from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWebEngineCore import *


from src.core.gui.uimanager import *

from src.components import *


class Layout(UiManager):
    eWebPage: QWebEngineView
    start_page_btn: QPushButton
    disable_element_btn: QPushButton
    inject_css_btn: QPushButton
    highlight_elm_btn: QPushButton
    design_mode_btn: QPushButton
    devtools_btn: QPushButton
    url_input: QLineEdit
    change_url_btn: QPushButton
    devtools_view: QWebEngineView

    def __init__(self):
        super().__init__()
        self.init_widgets()
        self.set_widgets()

        layout_data = [
            self.splitter("vertical", [
                "eWebPage",
                self.tabs(tab_labels=["Web Explore", "Web Editor", "Search Tools"], children=[
                    self.group("vertical", [
                        "start_page_btn",
                        "design_mode_btn",
                        "devtools_btn"
                    ]),
                    self.group("vertical", [
                        "disable_element_btn",
                        "inject_css_btn",
                        "highlight_elm_btn"
                    ]),
                    self.group("horizontal", [
                        "url_input",
                        "change_url_btn"
                    ])
                ])
            ])
        ]

        self.apply_layout(layout_data)

    def init_widgets(self):
        for name, widget_type in self.__annotations__.items():
            widget = widget_type()
            setattr(self, name, widget)

    def set_widgets(self):
        self.eWebPage.setUrl(QUrl("chrome://gpu"))
        self.start_page_btn.setText("Start WebPage")
        self.disable_element_btn.setText("Disable Element")
        self.inject_css_btn.setText("Inject Blue")
        self.highlight_elm_btn.setText("Highlight Element")
        self.design_mode_btn.setText("Activate Design Mode")
        self.devtools_btn.setText("Activate Dev Tools")
        self.url_input.setText("URL GOES HERE")
        self.change_url_btn.setText("Change to Entered URL")
        self.devtools_view.setWindowTitle("DevTools")