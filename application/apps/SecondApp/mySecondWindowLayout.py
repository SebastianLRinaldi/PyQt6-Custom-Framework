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

from application.core.Grouper.SpliterGroupConfiguration import *
from application.core.Grouper.TabGroupConfigureation import *
from application.core.Grouper.widgetGroupFrameworks import *

from application.core.Window.windowConfigureation import *

class SecondLayout(LayoutManager):
    def __init__(self):
        super().__init__()
        self.list_widget = QListWidget()
        self.name_label = QLabel(text="Enter your name:")
        self.text_edit = QTextEdit("This is a multi-line text editor")
        
        self.radio_button = QRadioButton(text="Select this option")
        self.check_box = QCheckBox(text="Accept terms and conditions")
        
        middleSplit = MasterSpliterGroup(orientation=Qt.Orientation.Vertical)
        labelsGroup = WidgetGroup(title="Random Labels")
        btnsGroup = WidgetGroup(title="Random Btns")
        
        self.add_widgets_to_window(
            middleSplit.add_widgets_to_spliter(
                labelsGroup.add_widgets_to_group(
                    self.name_label,
                    self.text_edit,
                    self.list_widget,
                ),

                btnsGroup.add_widgets_to_group(
                    self.radio_button,
                    self.check_box,
                )
            )
        )
