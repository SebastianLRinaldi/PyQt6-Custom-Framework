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


from application.FrontEnd.C_Grouper.SpliterGroupConfiguration import *
from application.FrontEnd.C_Grouper.TabGroupConfigureation import *
from application.FrontEnd.C_Grouper.WidgetGroupConfigureation import *

from application.FrontEnd.presentations.myFirstWindow.myFirstWindowWidgets import *
from application.FrontEnd.presentations.myFirstWindow.myFirstWindowConnections import *

from application.FrontEnd.D_WindowFolder.windowConfigureation import *
from application.FrontEnd.E_combiner.eventBus import *


window = Window(event_bus)


def my_first_page():
    
    window.window_layout_manager.add_widgets_to_window(
            middleSplit.add_widgets_to_spliter(
                
                calendar_widget,
                
                topTab.add_groups_as_tabs(
                    
                    exploreTab0.add_widgets_to_group(
                        list_widget,
                    ),
                    
                    playerControls.add_widgets_to_group(
                        button,
                        reset_button, 
                    ),
                ),
                
                bottomTab.add_groups_as_tabs(
                    
                        exploreTab1.add_widgets_to_group(
                            text_edit, 
                        ),
                        
                        exploreTab2.add_widgets_to_group(
                            radio_button,
                            label,  
                        ),
                        
                        exploreTab3.add_widgets_to_group(
                            check_box,
                        )
                    )
            )
        )
    
    
    window.window_layout_manager.show_window()






