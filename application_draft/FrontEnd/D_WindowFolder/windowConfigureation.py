from application_draft.FrontEnd.A_frameworks.gridLayoutFrameworks import *
from application_draft.FrontEnd.A_frameworks.widgetFrameworks import *
from application_draft.FrontEnd.E_combiner.eventBus import EventBus

from typing import Dict, TypeVar, Union

class WindowWidgetEventBusManager():
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.widgets: Dict[str, QWidget] = {}

    def register_widget(self, name: str, widget: QWidget) -> None:
        widget.setObjectName(name)
        self.widgets[name] = widget

class WindowLayoutManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Progressive FlashCards")
        self.resize(1000, 600)
        self.setup_stylesheets()

    def add_widgets_to_window(self, *widgets):
        grid_layout = GridLayout(*widgets, window=self.window)
        central_widget = Widget(grid_layout)
        self.setCentralWidget(central_widget)
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


class Window:
    def __init__(self, event_bus: EventBus):
        # Manager handling widgets and event bus
        self.window_event_bus = WindowWidgetEventBusManager(event_bus)
        # Layout manager for window layout setup
        self.window_layout_manager = WindowLayoutManager()
        
        