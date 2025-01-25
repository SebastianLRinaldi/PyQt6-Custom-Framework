from FrontEnd.C_Grouper.TabGroupBuilds.TabGroupBuilds import *
from FrontEnd.D_WindowFolder.WindowBuilds.windowBuild import *
from FrontEnd.C_Grouper.WidgetGroupBuilds.WidgetGroupBuild import *



class combiner():
    def __init__(self):
        exploreTab.add_widges_to_tab(
                    playerControls,
                    title="Search")



        window.setup_central_widget(
            exploreTab,
        )
        window.show_window()