from FrontEnd.B_WidgetsFolder.WidgetBuilds.WidgetBuild import *
from FrontEnd.C_Grouper.TabGroupBuilds.TabGroupBuilds import *
from FrontEnd.C_Grouper.WidgetGroupBuilds.WidgetGroupBuild import *
from FrontEnd.D_WindowFolder.WindowBuilds.windowBuild import *
from FrontEnd.E_combiner.connections import *

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

playerControls.add_widgets_to_group(
                button,
                table,
                tableLabel
                )


class combiner():
    def __init__(self):
        exploreTab.add_widges_to_tab(
            playerControls,
            title="Search")
        
        # exploreTab.add_widges_to_tab(
        #     playerControls2,
        #     title="Search2"
        # )
        
        # exploreTab1.add_widges_to_tab(
        #     playerControls1,
        #     title="Search1")



        window.add_widgets_to_window(
            exploreTab,
            # exploreTab1
        )
        window.show_window()