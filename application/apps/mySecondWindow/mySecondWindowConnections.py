from application.FrontEnd.apps.mySecondWindow.mySecondWindowWidgets import *
from application.FrontEnd.apps.mySecondWindow.mySecondWindowFunctions import*
from application.FrontEnd.apps.mySecondWindow.mySecondWindowLayout import *
from application.FrontEnd.E_combiner.eventBus import *


# button.clicked.connect(event_bus.eventTriggered.emit)
event_bus.widget_update_requested.connect(update_label)
event_bus.widget_reset_requested.connect(reset_label)

# reset_button.clicked.connect(reset_label)










