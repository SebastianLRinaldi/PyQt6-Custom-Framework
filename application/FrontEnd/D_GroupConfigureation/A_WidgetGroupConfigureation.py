from FrontEnd.A_frameworks.widgetGroupFrameworks import WidgetGroup
from FrontEnd.C_WidgetBuild.singleWidgetBuilds import button, tableLabel




class PlayerControls(WidgetGroup):
    def __init__(self, widgetRow = -1, widgetCol = -1):
        super().__init__(widgetRow, widgetCol)
        
        # Create and arrange buttons/widgets specific to PlayerControls
        self.set_grid_layout(
            button,
            tableLabel
            
            # PlayButtn(self.ui_handler, widgetRow=0, widgetCol=0, widgetRowSpan=1, widgetColSpan=2),  # Pass window and UIHandler
            # PrevousTrackButtn(self.ui_handler, widgetRow=1, widgetCol=0, widgetRowSpan=1, widgetColSpan=1),
            # NextTrackButtn(self.ui_handler, widgetRow=1, widgetCol=1, widgetRowSpan=1, widgetColSpan=1)
        )





