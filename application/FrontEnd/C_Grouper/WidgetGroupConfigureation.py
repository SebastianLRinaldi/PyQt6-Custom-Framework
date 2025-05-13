from application.FrontEnd.A_frameworks.widgetGroupFrameworks import WidgetGroup


"""
Like in our tabs we don't want to know the widgets when we crate it, we just want to make the group later with the build widgets later
want to build a add widgets functions basically
"""

class PlayerControls(WidgetGroup):
    def __init__(self, title=None, widgetRow = -1, widgetCol = -1):
        super().__init__(title, widgetRow, widgetCol)
        
        
        

# playerControls = PlayerControls(title="Player Controls")
# searchControls = WidgetGroup(title="Search Controls")

# exploreTab0 = WidgetGroup(title="search0")
# exploreTab1 = WidgetGroup(title="search1")
# exploreTab2 = WidgetGroup(title="search2")
# exploreTab3 = WidgetGroup(title="search3")



