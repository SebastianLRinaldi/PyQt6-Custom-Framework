from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from src.helpers import *
from .bundle import Bundle

"""
Close methods
Ctrl+k + Ctrl+0

Open Methods 
Ctrl+k + Ctrl+J
"""
class Logic(Bundle):

    def __init__(self, component):
        self._map_widgets(component)
