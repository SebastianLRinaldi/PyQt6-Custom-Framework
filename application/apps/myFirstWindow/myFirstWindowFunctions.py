from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *


from application.apps.myFirstWindow.myFirstWindowLayout import My_First_Page


class FirstPageLogic:
    def __init__(self, ui: My_First_Page):
        self.ui = ui

    def update_widget(self) -> None:
        self.ui.label.setText("Im on 1, I have been updated by 1!")

    def reset_widget(self) -> None:
        self.ui.label.setText("Im on 1, I have been reset by 1!")

    
