from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

class Tab(QTabWidget):
    def __init__(self, title="New Tab", widgetRow=-1, widgetCol=-1, widgetRowSpan=-1, widgetColSpan=-1 ):
        super().__init__()
        self.parent = None
        self.title = title
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        self.widgetRowSpan = widgetRowSpan 
        self.widgetColSpan = widgetColSpan 
        
    def set_MainWindow(self, window: QMainWindow):
        self.parent = window
        
    def add_widges_to_tab(self, *widgets):
        new_tab = QWidget()
        layout = QGridLayout(new_tab)
        
        for i, widget in enumerate(widgets):
            widgetRow = widget.widgetRow #i // 1
            widgetCol = widget.widgetCol#i % 1
            
            # print(f'TAB: {type(widget)}')
            if widgetRow == -1 or widgetCol == -1:
                widgetRow = i // 1
                widgetCol = i % 1
                layout.addWidget(widget, widgetRow, widgetCol)
            else:
                layout.addWidget(widget, widgetRow, widgetCol)
            
        self.addTab(new_tab, self.title)
        self.setTabShape(QTabWidget.TabShape.Triangular)
        self.setMovable(True)
        return self



