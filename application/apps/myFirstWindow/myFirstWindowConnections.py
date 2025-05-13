from application.apps.myFirstWindow.myFirstWindowFunctions import*

class FirstPageConnections:
    def __init__(self, ui: My_First_Page, logic: FirstPageLogic):
        self.ui = ui
        self.logic = logic

        self.ui.start_page_btn.clicked.connect(lambda: self.logic.load_url("https://open.spotify.com/embed/playlist/37i9dQZEVXcRbPtT6vrrSL"))
        self.ui.debug_page_btn.clicked.connect(lambda: self.logic.disable_element("/html/body/div/div/div/div[4]"))
        self.ui.inject_css_btn.clicked.connect(lambda:self.logic.inject_css("/html/body"))
        self.ui.highlight_elm_btn.clicked.connect(lambda:self.logic.highlight_element("/html/body/div/div/div/div[1]/div[1]/div"))
        self.ui.design_mode_btn.clicked.connect(self.logic.activate_design_mode)
        self.ui.devtools_btn.clicked.connect(self.logic.activate_devtools)


        self.ui.change_url_btn.clicked.connect(self.logic.change_url)


# from application.apps.myFirstWindow.myFirstWindowWidgets import *
# from application.apps.myFirstWindow.myFirstWindowFunctions import*
# from application.FrontEnd.presentations.myFirstWindow.myFirstWindowLayout import *
# from application.FrontEnd.E_combiner.eventBus import *


# update_widget_btn.clicked.connect(event_bus.widget_update_requested.emit)
# reset_widget_btn.clicked.connect(event_bus.widget_reset_requested.emit)

# event_bus.widget_update_requested.connect(update_widget)
# event_bus.widget_reset_requested.connect(reset_widget)



# start_page_btn.clicked.connect(lambda: load_url("https://open.spotify.com/embed/playlist/37i9dQZEVXcRbPtT6vrrSL"))
# debug_page_btn.clicked.connect(lambda: disable_element("/html/body/div/div/div/div[4]"))
# inject_css_btn.clicked.connect(lambda:inject_css("/html/body"))
# highlight_elm_btn.clicked.connect(lambda:highlight_element("/html/body/div/div/div/div[1]/div[1]/div"))
# design_mode_btn.clicked.connect(activate_design_mode)
# devtools_btn.clicked.connect(activate_devtools)


# change_url_btn.clicked.connect(change_url)
















# start_page_btn.clicked.connect(start_page)
# debug_page_btn.clicked.connect(debug_page)




# event_bus.eventTriggered.connect(update_label)


# reset_button.clicked.connect(reset_label)

