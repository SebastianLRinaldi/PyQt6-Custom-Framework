from application.apps.myThirdWindow.myThirdWindowFunctions import*

class ThirdPageConnections:
    def __init__(self, ui: My_Third_Page, logic: ThirdPageLogic):
        self.ui = ui
        self.logic = logic
    #     self.connect_signals()

    # def connect_signals(self):
    #     self.ui.update_widget_btn.clicked.connect(self.logic.some_method)