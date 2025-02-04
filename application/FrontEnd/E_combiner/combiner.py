from application.FrontEnd.B_WidgetsFolder.WidgetInitializations.WidgetInitialization import *
from application.FrontEnd.C_Grouper.TabGroupInitializations.TabGroupInitialization import *
from application.FrontEnd.C_Grouper.WidgetGroupInitializations.WidgetGroupInitialization import *
from application.FrontEnd.D_WindowFolder.WindowInitializations.windowInitialization import *
from application.FrontEnd.E_combiner.connections import *

"""
Basically want to see the nested widgets and tabs and groups
- also fix it so that it sasys widgets not widges
        exploreTab.add_widges_to_tab(
                    playerControls.add_widges_to_group(
                        button,
                        label,
                        table
                    ),
                    title="Search")


"""


class combiner():
    def __init__(self):

        window.add_widgets_to_window(
            calendar_widget,
            check_box,
            exploreMasterTab.add_widgets_as_seperate_tabs(
                exploreTab0.add_widgets_to_group(
                    text_edit,
                    list_widget,
                ),
                playerControls.add_widgets_to_group(
                    button,  
                ),
                exploreTab1.add_widgets_to_group(
                    label,
                ),
            ),

            exploreTab2.add_widgets_to_group(
                radio_button,
            )
        )
        window.show_window()
        
        
        
"""
class combiner():
    def __init__(self):

        window.add_widgets_to_window(
            calendar_widget,
            check_box,
            exploreTab.add_widges_to_tab(
                text_edit,
                exploreTab1.add_widges_to_tab(
                    label,
                    playerControls.add_widgets_to_group(
                        button,
                        ),
                ),
            ),
            exploreTab.add_widges_to_tab(
                list_widget,
            ),
            exploreTab2.add_widges_to_tab(
                radio_button,
            )
        )
        window.show_window()
""" 