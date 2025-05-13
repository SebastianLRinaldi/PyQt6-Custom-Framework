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


from application.FrontEnd.C_Grouper.SpliterGroupConfiguration import *
# from application.FrontEnd.C_Grouper.TabGroupConfigureation import *
# from application.FrontEnd.C_Grouper.WidgetGroupConfigureation import *

# from application.FrontEnd.presentations.myFirstWindow.myFirstWindowWidgets import *
# from application.FrontEnd.presentations.myFirstWindow.myFirstWindowConnections import *

from application.FrontEnd.D_WindowFolder.windowConfigureation import *
# from application.FrontEnd.E_combiner.eventBus import *


# window = Window(event_bus)


# def my_first_page():
    
#     window.window_layout_manager.add_widgets_to_window(
#             middleSplit.add_widgets_to_spliter(
                
#                 calendar_widget,
#                 eWebPage,
                
#                 topTab.add_groups_as_tabs(
#                     playerControls.add_widgets_to_group(
#                         start_page_btn,
#                         debug_page_btn,
#                         inject_css_btn,
#                         highlight_elm_btn,
#                         design_mode_btn,
#                         devtools_btn,
#                     ),
                    
                    
#                     searchControls.add_widgets_to_group(
#                         url_input,
#                         change_url_btn,
                        
#                     ),
                    
                    
#                     exploreTab0.add_widgets_to_group(
#                         list_widget,
#                         update_widget_btn,
#                         reset_widget_btn, 
                        
#                     ),
                    
#                 ),
                
#                 bottomTab.add_groups_as_tabs(
                    
#                         exploreTab1.add_widgets_to_group(
#                             text_edit, 
#                         ),
                        
#                         exploreTab2.add_widgets_to_group(
#                             radio_button,
#                             label,  
#                         ),
                        
#                         exploreTab3.add_widgets_to_group(
#                             check_box,
#                         )
#                     )
#             )
#         )
    
    
#     window.window_layout_manager.show_window()


# class First_window_widgets():
#     update_widget_btn = Button(text="Start")
#     reset_widget_btn = Button(text="Reset")

#     label = Label(text="Enter your name:")
#     check_box = CheckBox(text="Accept terms and conditions")
#     radio_button = RadioButton(text="Select this option")
#     calendar_widget = CalendarWidget()
#     list_widget = ListWidget()
#     text_edit = TextEdit(text="This is a multi-line text editor")

#     eWebPage = WebPage()
#     start_page_btn = Button(text="Start WebPage")
#     debug_page_btn = Button(text="Show WebPage Debug Data")
#     inject_css_btn = Button(text="Inject Blue")
#     highlight_elm_btn = Button(text="Highlight Element")
#     design_mode_btn = Button(text="Activate Design Mode")
#     devtools_btn =  Button(text="Activate Dev Tools")




#     url_input = QLineEdit(text="URL GOES HERE")
#     change_url_btn = QPushButton(text="Change to Entered URL")




    # DevTools view
    # devtools_view = WebPage()
    # devtools_view.setWindowTitle("DevTools")
# from types import SimpleNamespace

# widgets = SimpleNamespace(
#     update=QPushButton(text="Start"),
#     reset=QPushButton(text="Reset")
# )

class My_First_Page(AppLayoutManager):
    def __init__(self):
        super().__init__()

        self.update_widget_btn = QPushButton(text="Start")
        reset_widget_btn = QPushButton(text="Reset")

        self.label = QLabel(text="Enter your name:")
        self.check_box = QCheckBox(text="Accept terms and conditions")
        self.radio_button = QRadioButton(text="Select this option")
        self.calendar_widget = QCalendarWidget()
        self.list_widget = QListWidget()
        self.text_edit = QTextEdit("This is a multi-line text editor")

        self.eWebPage = QWebEngineView()
        self.start_page_btn = QPushButton(text="Start WebPage")
        self.debug_page_btn = QPushButton(text="Show WebPage Debug Data")
        self.inject_css_btn = QPushButton(text="Inject Blue")
        self.highlight_elm_btn = QPushButton(text="Highlight Element")
        self.design_mode_btn = QPushButton(text="Activate Design Mode")
        self.devtools_btn =  QPushButton(text="Activate Dev Tools")




        self.url_input = QLineEdit(text="URL GOES HERE")
        self.change_url_btn = QPushButton(text="Change to Entered URL")




        # DevTools view
        self.devtools_view = QWebEngineView()
        self.devtools_view.setWindowTitle("DevTools")

        middleSplit = MasterSpliterGroup(orientation=Qt.Orientation.Vertical)

        
        # window = Window(event_bus)
        self.add_widgets_to_window(
            self.update_widget_btn,
            reset_widget_btn,

            middleSplit.add_widgets_to_spliter(
                self.calendar_widget,
                self.eWebPage,
                self.start_page_btn,
            )
        )
                

