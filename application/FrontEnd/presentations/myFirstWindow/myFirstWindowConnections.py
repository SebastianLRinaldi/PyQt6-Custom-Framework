from application.FrontEnd.presentations.myFirstWindow.myFirstWindowWidgets import *
from application.FrontEnd.presentations.myFirstWindow.myFirstWindowFunctions import*
from application.FrontEnd.presentations.myFirstWindow.myFirstWindowLayout import *
from application.FrontEnd.E_combiner.eventBus import *


button.clicked.connect(event_bus.update_widget.emit)
reset_button.clicked.connect(event_bus.reset_widget.emit)

event_bus.update_widget.connect(update_label)
event_bus.reset_widget.connect(reset_label)


# event_bus.eventTriggered.connect(update_label)


# reset_button.clicked.connect(reset_label)










