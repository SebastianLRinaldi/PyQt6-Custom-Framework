from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *



class WidgetGroup(QWidget):
    def __init__(self, title=None, widgetRow=-1, widgetCol=-1, widgetRowSpan=-1, widgetColSpan=-1):
        super().__init__()
        # self.ui_handler = UIHandler(window)  # Create UIHandler instance directly
        self.window = None  # Store reference to the QMainWindow instance
        self.widgetRow = widgetRow  # Row position in layout
        self.widgetCol = widgetCol  # Column position in layout
        self.widgetRowSpan = widgetRowSpan 
        self.widgetColSpan = widgetColSpan 

        self.title = title

    def add_widgets_to_group(self, *widgets, setlayout:str=None):
        if setlayout is "QVBox" or setlayout is None:
            layout = QVBoxLayout()
            for index, widget in enumerate(widgets):
                layout.addWidget(widget)
            self.setLayout(layout)

        elif setlayout is "QHBox":
            layout = QHBoxLayout()
            for index, widget in enumerate(widgets):
                layout.addWidget(widget)
            self.setLayout(layout)
            
        return self
        
    def set_MainWindow(self, window: QMainWindow):
        self.window = window