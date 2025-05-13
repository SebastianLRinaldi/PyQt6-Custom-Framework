from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

from PyQt6.QtWidgets import QTabWidget, QWidget, QGridLayout, QMainWindow
from typing import List, Optional


from application.FrontEnd.C_Grouper.WidgetGroupConfigureation import WidgetGroup

class TabHolder(QTabWidget):
    def __init__(
        self,
        widgetRow: int = -1,
        widgetCol: int = -1,
        widgetRowSpan: int = -1,
        widgetColSpan: int = -1,
        title: str = "",
    ):
        super().__init__()
        self._parent = None
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        self.widgetRowSpan = widgetRowSpan
        self.widgetColSpan = widgetColSpan
        self.title = title
        self.setTabShape(QTabWidget.TabShape.Triangular)
        self.setMovable(True)
        
    def set_main_window(self, window: QMainWindow) -> None:
        """Set the main window parent."""
        self._parent = window
    
    @property
    def parent_window(self) -> Optional[QMainWindow]:
        return self._parent
    
    def add_groups_as_tabs(self, *pages: WidgetGroup):
        """Add tabs to the master tab widget for the group of widgets as pages"""
        for page in pages:
            if page.title:
                self.addTab(page, page.title)
            else:
                self.addTab(page, "EMPTY")
        return self
   

topTab = TabHolder(title="Inputs")
bottomTab = TabHolder(title="btns")

