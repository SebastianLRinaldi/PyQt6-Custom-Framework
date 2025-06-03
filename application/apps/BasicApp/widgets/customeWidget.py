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
from PyQt6.QtMultimedia import *
from PyQt6.QtMultimediaWidgets import *

from application.core.Grouper.SpliterGroupConfiguration import *
from application.core.Grouper.TabGroupConfigureation import *
from application.core.Grouper.widgetGroupFrameworks import *

from application.core.Window.windowConfigureation import *


class MediaBtnControls(LayoutManager):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Media Controls")
