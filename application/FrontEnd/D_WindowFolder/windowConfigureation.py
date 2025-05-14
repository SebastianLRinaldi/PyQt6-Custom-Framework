from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *
# from application.FrontEnd.E_combiner.eventBus import EventBus

from typing import Dict, TypeVar, Union

# class WindowWidgetEventBusManager():
#     def __init__(self, event_bus: EventBus):
#         self.event_bus = event_bus
#         self.widgets: Dict[str, QWidget] = {}

#     def register_widget(self, name: str, widget: QWidget) -> None:
#         widget.setObjectName(name)
#         self.widgets[name] = widget

class AppLayoutManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Progressive FlashCards")
        self.resize(1000, 600)
        self.setup_stylesheets()

    def add_widgets_to_window(self, *widgets, setlayout:str=None):
        if setlayout == "QVBox" or setlayout == None:
            layout = QVBoxLayout()
            for index, widget in enumerate(widgets):
                layout.addWidget(widget)
            self.setLayout(layout)

        elif setlayout == "QHBox":
            layout = QHBoxLayout()
            for index, widget in enumerate(widgets):
                layout.addWidget(widget)
            self.setLayout(layout)
            
        return self

    def show_window(self):
        self.show()

    def setup_stylesheets(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a0d1c;
            }
            QLabel {
                background-color: #AAAAAA;
            }
        """)

# class Window:
#     def __init__(self, event_bus: EventBus):
#         # Manager handling widgets and event bus
#         self.window_event_bus = WindowWidgetEventBusManager(event_bus)
#         # Layout manager for window layout setup
#         self.window_layout_manager = AppLayoutManager()
        
        