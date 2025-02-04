from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

from PyQt6.QtWidgets import QTabWidget, QWidget, QGridLayout, QMainWindow
from typing import List, Optional

class MasterTabHolder(QTabWidget):
    def __init__(
        self,
        widgetRow: int = -1,
        widgetCol: int = -1,
        widgetRowSpan: int = -1,
        widgetColSpan: int = -1
    ):
        super().__init__()
        self._parent = None
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        self.widgetRowSpan = widgetRowSpan
        self.widgetColSpan = widgetColSpan
        
    def set_main_window(self, window: QMainWindow) -> None:
        """Set the main window parent."""
        self._parent = window
    
    @property
    def parent_window(self) -> Optional[QMainWindow]:
        return self._parent
    
    def add_widgets_as_seperate_tabs(self, *tabs: QWidget):
        """Add tabs to the master holder and return their indices."""
        for tab in tabs:
            self.addTab(tab, tab.title)
        return self
   



