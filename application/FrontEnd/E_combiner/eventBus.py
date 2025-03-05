from PyQt6.QtCore import QObject, pyqtSignal, QThread
from typing import Dict, TypeVar, Union
from queue import Queue



class EventBus(QObject):
    update_widget = pyqtSignal()
    reset_widget = pyqtSignal()
    
    # def __init__(self):
    #     pass

event_bus = EventBus()