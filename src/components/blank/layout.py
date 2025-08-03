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

from src.core.gui.ui_manager import *
from src.components import *


class Layout(UiManager):

    def __init__(self):
        super().__init__()
        self.init_widgets()
        self.set_widgets()

        layout_data = []

        self.apply_layout(layout_data)

    def init_widgets(self):
        for name, widget_type in self.__annotations__.items():
            widget = widget_type()
            setattr(self, name, widget)

    def set_widgets(self):
        pass






