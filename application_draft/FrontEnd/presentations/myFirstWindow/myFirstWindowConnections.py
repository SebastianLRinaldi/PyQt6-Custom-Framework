from application_draft.FrontEnd.presentations.myFirstWindow.myFirstWindowWidgets import *
from application_draft.FrontEnd.presentations.myFirstWindow.myFirstWindowFunctions import*
from application_draft.FrontEnd.presentations.myFirstWindow.myFirstWindowLayout import *
from application_draft.FrontEnd.E_combiner.eventBus import *


button.clicked.connect(event_bus.eventTriggered.emit)
event_bus.eventTriggered.connect(update_label)











