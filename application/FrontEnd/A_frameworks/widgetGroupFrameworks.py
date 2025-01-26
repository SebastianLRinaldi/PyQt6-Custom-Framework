from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from FrontEnd.A_frameworks.gridLayoutFrameworks import GridLayout
class WidgetGroup(QWidget):
    def __init__(self, widgetRow = -1, widgetCol = -1):
        super().__init__()
        # self.ui_handler = UIHandler(window)  # Create UIHandler instance directly
        self.window = None  # Store reference to the QMainWindow instance
        self.widgetRow = widgetRow  # Row position in layout
        self.widgetCol = widgetCol  # Column position in layout

    def add_widgets_to_group(self, *widgets):
        grid_layout = GridLayout(*widgets)  # Arrange widgets in grid
        self.setLayout(grid_layout)  # Set the layout of the widget
        
    def set_MainWindow(self, window: QMainWindow):
        self.window = window