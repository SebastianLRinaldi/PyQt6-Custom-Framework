import os
import sys
import time
import re

import threading
from threading import Thread
from enum import Enum
from queue import Queue
from typing import List
from datetime import timedelta

from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

from FrontEnd.A_frameworks.widgetFrameworks import ConnectedWidget, IsolatedWidget

class Button(QPushButton, ConnectedWidget):
    def __init__(self, text="Click me!", widgetRow=-1, widgetCol=-1, widgetRowSpan=-1, widgetColSpan=-1):
        super().__init__(text)
        self.widgetRow = widgetRow
        self.widgetCol = widgetCol
        
class TrackTableLabel(QLabel, IsolatedWidget):
    def __init__(self, text="track_label", widgetRow=-1, widgetCol=-1):
        super().__init__(widgetRow=widgetRow, widgetCol=widgetCol)
        QLabel.__init__(self, text)

class TrackTabel(QListWidget, ConnectedWidget):
    def __init__(self, ui_handler, widgetRow=-1, widgetCol=-1):
        super().__init__(ui_handler, widgetRow, widgetCol)
        QListWidget.__init__(self)

    #     self.itemClicked.connect(self.on_item_clicked)
        
    # def on_item_clicked(self, item: TrackItem):
    #     print(f"TrackObject: {item}")
    #     self.ui_handler.ClickedTrack(item)