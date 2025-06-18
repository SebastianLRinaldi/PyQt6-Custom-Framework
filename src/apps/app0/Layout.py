from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from src.core.Grouper.SpliterGroupConfiguration import *
from src.core.Grouper.TabGroupConfigureation import *
from src.core.Grouper.widgetGroupFrameworks import *


from src.core.GUI.UiManger import *

# from .widgets.CUSTOMWIDGET import YOURWIDGET



"""
When you press enter after you type it should either go to the category selection or the next text box below
"""
class Layout(UiManager):
    def __init__(self):
        super().__init__()