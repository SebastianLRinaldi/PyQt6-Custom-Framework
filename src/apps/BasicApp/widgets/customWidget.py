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
from PyQt6.QtMultimedia import *
from PyQt6.QtMultimediaWidgets import *

from src.core.Grouper.SpliterGroupConfiguration import *
from src.core.Grouper.TabGroupConfigureation import *
from src.core.Grouper.widgetGroupFrameworks import *

from src.core.Window.windowConfigureation import *


class CustomWidget(LayoutManager):

    label: QLabel
    list: QListWidget
    btn: QPushButton


    def __init__(self):
        super().__init__()
        self.init_widgets()
        self.setWindowTitle("Custom Widget")
        self.label.setText("Header Label")

        self.btn.setText("Action")

    def init_widgets(self):
        for name, widget_type in self.__annotations__.items():
            setattr(self, name, widget_type())

        layout_data = [
            self.group("horizontal",["label"]),
            self.group("vertical",["list", "btn"]),
            

        
        ]

        self.apply_layout(layout_data)



