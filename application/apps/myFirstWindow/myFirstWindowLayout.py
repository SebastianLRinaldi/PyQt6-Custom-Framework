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


from application.FrontEnd.C_Grouper.SpliterGroupConfiguration import *
from application.FrontEnd.C_Grouper.TabGroupConfigureation import *
from application.FrontEnd.C_Grouper.widgetGroupFrameworks import *



from application.FrontEnd.D_WindowFolder.windowConfigureation import *



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


# from PyQt6.QtWebEngineCore import QWebEngineUrlRequestInterceptor

# class AdBlockInterceptor(QWebEngineUrlRequestInterceptor):
#     def interceptRequest(self, info):
#         url = info.requestUrl().toString()
#         if self.should_block(url):
#             info.block(True)

#     def should_block(self, url: str) -> bool:
#         block_keywords = [
#             "ads", "adservice", "doubleclick", "googlesyndication",
#             "tracking", "pixel", "analytics", "clicktracker",
#             "facebook.net", "beacon", "sponsor", "promo"
#         ]
#         return any(word in url for word in block_keywords)




class My_First_Page(AppLayoutManager):
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
                

