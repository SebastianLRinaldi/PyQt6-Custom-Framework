from application.FrontEnd.presentations.myFirstWindow.myFirstWindowWidgets import *
from application.FrontEnd.presentations.myFirstWindow.myFirstWindowFunctions import*
from application.FrontEnd.presentations.myFirstWindow.myFirstWindowLayout import *
from application.FrontEnd.E_combiner.eventBus import *


update_widget_btn.clicked.connect(event_bus.widget_update_requested.emit)
reset_widget_btn.clicked.connect(event_bus.widget_reset_requested.emit)

event_bus.widget_update_requested.connect(update_widget)
event_bus.widget_reset_requested.connect(reset_widget)



start_page_btn.clicked.connect(lambda: load_url("https://open.spotify.com/embed/playlist/25zTI6PRLPTVszmq5WhC8c?utm_source=generator"))
debug_page_btn.clicked.connect(lambda: disable_element("/html/body/div/div/div/div[4]"))
# start_page_btn.clicked.connect(start_page)
# debug_page_btn.clicked.connect(debug_page)




# event_bus.eventTriggered.connect(update_label)


# reset_button.clicked.connect(reset_label)










