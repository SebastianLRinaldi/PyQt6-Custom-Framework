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


from src.core.Window.windowConfigureation import *

from .widgets.customWidget import CustomWidget


class BasicLayout(LayoutManager):
    
    another_widget:CustomWidget
    label: QLabel
    list: QListWidget
    btn: QPushButton

    def __init__(self):
        super().__init__()
        self.init_widgets()
        self.label.setText("Header: Word Analysis")
        self.btn.setText("Main Action")


    # def init_widgets(self):
    #     for name, widget_type in self.__annotations__.items():
    #         setattr(self, name, widget_type())

    def init_widgets(self):
        for name, widget_type in self.__annotations__.items():
            widget = widget_type()
            if isinstance(widget, QListWidget):
                widget.setFlow(QListWidget.Flow.LeftToRight)
                widget.setWrapping(True)
                widget.setResizeMode(QListWidget.ResizeMode.Adjust)
                widget.addItems([f"{name}_item{i}" for i in range(5)])
            setattr(self, name, widget)




        layout_data = [
            # "btn",
            # "another_widget",
            # "label"
            "another_widget",
            self.splitter("vertical", ["label", "list",]),
            self.tabs(["list", self.grid(["btn"], 1, 2)])

            
        ]


        self.apply_layout(layout_data)
        self.print_margins_recursive(self)






