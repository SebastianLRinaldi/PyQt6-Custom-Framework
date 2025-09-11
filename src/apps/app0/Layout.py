from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from src.core.gui.ui_manager import *
from .bundle import Bundle

class Layout(UiManager, Bundle):
    def __init__(self, component):
        super().__init__()
        self._map_widgets(component)
        self.set_widgets()
        self.setup_stylesheets()

        layout_data = [
            
            self.box("vertical", "Apps Widgets", [self.btn1]),

            self.box("vertical", "External App", [self.another_widget.layout]),

            self.box("vertical", "WEB", [self.web_widget.layout]),
            
            
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
        
