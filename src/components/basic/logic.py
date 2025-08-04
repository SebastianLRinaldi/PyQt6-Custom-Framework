from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from .layout import Layout
# from src.components import YourNeededLayoutLogicConnection
from src.helpers import *

class Logic:
    def __init__(self, ui: Layout):
        self.ui = ui

    def update_widget(self) -> None:
        self.ui.label.setText("Im on 1, I have been updated by 1!")

    def reset_widget(self) -> None:
        self.ui.label.setText("Im on 1, I have been reset by 1!")
        