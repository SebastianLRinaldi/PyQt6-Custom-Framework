from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from src.core.gui.ui_manager import *
from src.components import *

class Layout(UiManager):

    btn1: QPushButton
    another_widget: Basic
    web_widget: Web
    
    def __init__(self):
        super().__init__()
        self.init_widgets()
        self.setup_stylesheets()
        self.set_widgets()

        layout_data = [
            self.box("vertical", "Apps Widgets", ["btn1"]),

            self.box("vertical", "External component in this App", [self.another_widget.layout]),

            self.box("vertical", "EWEB", [self.web_widget.layout]),
            
            
        ]

        self.apply_layout(layout_data)

    def init_widgets(self):
        annotations = getattr(self.__class__, "__annotations__", {})
        for name, widget_type in annotations.items():
            widget = widget_type()
            setattr(self, name, widget)
            
    def setup_stylesheets(self):
        self.setStyleSheet(""" """)

    def set_widgets(self):
        self.btn1.setText("Push Me!")
        
