from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from .layout import Layout

"""
Close methods
Ctrl+k + Ctrl+0

Open Methods 
Ctrl+k + Ctrl+J
"""

class Logic:
    def __init__(self, ui: Layout):
        self.ui = ui