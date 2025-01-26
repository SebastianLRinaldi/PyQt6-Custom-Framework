from FrontEnd.A_frameworks.widgetGroupFrameworks import WidgetGroup


"""
Like in our tabs we don't want to know the widgets when we crate it, we just want to make the group later with the build widgets later
want to build a add widgets functions basically
"""

class PlayerControls(WidgetGroup):
    def __init__(self, widgetRow = -1, widgetCol = -1):
        super().__init__(widgetRow, widgetCol)
        
        # Create and arrange buttons/widgets specific to PlayerControls
        # self.set_grid_layout(
        #     button,
        #     table,
        #     tableLabel,
            
        # )

class PlayerControls1(WidgetGroup):
    def __init__(self, widgetRow = -1, widgetCol = -1):
        super().__init__(widgetRow, widgetCol)
        
        # Create and arrange buttons/widgets specific to PlayerControls
        # self.set_grid_layout(
        #     button1,
        #     tableLabel1,
        # )
        
        
class PlayerControls2(WidgetGroup):
    def __init__(self, widgetRow = -1, widgetCol = -1):
        super().__init__(widgetRow, widgetCol)
        
        # Create and arrange buttons/widgets specific to PlayerControls
        # self.set_grid_layout(
        #     button2,
        #     tableLabel2,
        # )





