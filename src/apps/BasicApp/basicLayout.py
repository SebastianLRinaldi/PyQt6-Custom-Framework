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

from src.core.Grouper.SpliterGroupConfiguration import *
from src.core.Grouper.TabGroupConfigureation import *
from src.core.Grouper.widgetGroupFrameworks import *

from src.core.Window.windowConfigureation import *

class BasicLayout(LayoutManager):
    def __init__(self):
        super().__init__()

        self.update_widget_btn = QPushButton(text="Start")
        self.reset_widget_btn = QPushButton(text="Reset")

        self.label = QLabel(text="Enter your name:")
        self.check_box = QCheckBox(text="Accept terms and conditions")
        self.radio_button = QRadioButton(text="Select this option")
        self.calendar_widget = QCalendarWidget()
        self.list_widget = QListWidget()
        self.text_edit = QTextEdit("This is a multi-line text editor")

        middleSplit = MasterSpliterGroup(orientation=Qt.Orientation.Vertical)

        btnGroup = WidgetGroup(title="Web Explore")
        # window = Window(event_bus)
        self.add_widgets_to_window(

            middleSplit.add_widgets_to_spliter(
                self.calendar_widget,

                btnGroup.add_widgets_to_group(
                    self.update_widget_btn,
                    self.reset_widget_btn,
                )
            )
        )
                

