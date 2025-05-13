from PyQt6.QtCore import QObject, pyqtSignal, QThread
from typing import Dict, TypeVar, Union
from queue import Queue



class EventBus(QObject):
    widget_update_requested = pyqtSignal()
    widget_reset_requested = pyqtSignal()
    
    # def __init__(self):
    #     pass

event_bus = EventBus()