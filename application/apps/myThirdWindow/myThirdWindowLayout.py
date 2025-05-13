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


# from application.FrontEnd.C_Grouper.SpliterGroupConfiguration import *
# from application.FrontEnd.C_Grouper.TabGroupConfigureation import *
# from application.FrontEnd.C_Grouper.WidgetGroupConfigureation import *

# from application.FrontEnd.presentations.myFirstWindow.myFirstWindowWidgets import *
# from application.FrontEnd.presentations.myFirstWindow.myFirstWindowConnections import *

from application.FrontEnd.D_WindowFolder.windowConfigureation import *
# from application.FrontEnd.E_combiner.eventBus import *


class My_Third_Page(AppLayoutManager):
    def __init__(self):
        super().__init__()

        self.update_widget_btn = QPushButton(text="Start")
        reset_widget_btn = QPushButton(text="Reset")

        self.label = QLabel(text="Enter your name:")
        check_box = QCheckBox(text="Accept terms and conditions")
        radio_button = QRadioButton(text="Select this option")
        calendar_widget = QCalendarWidget()
        list_widget = QListWidget()
        text_edit = QTextEdit("This is a multi-line text editor")

        # eWebPage = WebPage()
        start_page_btn = QPushButton(text="Start WebPage")
        debug_page_btn = QPushButton(text="Show WebPage Debug Data")
        inject_css_btn = QPushButton(text="Inject Blue")
        highlight_elm_btn = QPushButton(text="Highlight Element")
        design_mode_btn = QPushButton(text="Activate Design Mode")
        devtools_btn =  QPushButton(text="Activate Dev Tools")




        url_input = QLineEdit(text="URL GOES HERE")
        change_url_btn = QPushButton(text="Change to Entered URL")




        # DevTools view
        # devtools_view = WebPage()
        # devtools_view.setWindowTitle("DevTools")

        # middleSplit = MasterSpliterGroup(orientation=Qt.Orientation.Vertical)

        
        # window = Window(event_bus)
        self.add_widgets_to_window(
            self.label,
            reset_widget_btn

            # middleSplit.add_widgets_to_spliter(
                # calendar_widget,
                # eWebPage,
            # )
        )