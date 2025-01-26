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
            check_box,
            exploreTab1.add_widges_to_tab(
                text_edit,
                exploreTab.add_widges_to_tab(
                    label,
                    playerControls.add_widgets_to_group(
                        button,
                        ),
                    title="Search2"
                ),
                title="Search1"
            )
        )
        window.show_window()