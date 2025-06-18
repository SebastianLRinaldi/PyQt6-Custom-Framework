from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from src.core.Grouper.SpliterGroupConfiguration import *
from src.core.Grouper.TabGroupConfigureation import *
from src.core.Grouper.widgetGroupFrameworks import *


from src.core.GUI.UiManger import *

# from .widgets.CUSTOMWIDGET import YOURWIDGET


class Layout(UiManager):

    # name : QWidget

    
    def __init__(self):
        super().__init__()
        self.init_widgets()


        layout_data = [
    
        ]

        self.apply_layout(layout_data)


    def init_widgets(self):
        for name, widget_type in self.__annotations__.items():
            widget = widget_type()
            setattr(self, name, widget)