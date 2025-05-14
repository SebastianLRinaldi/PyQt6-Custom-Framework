from application.apps.mySecondWindow.mySecondWindowFunctions import*

class SecondPageConnections:
    def __init__(self, ui: My_Second_Page, logic: SecondPageLogic):
        self.ui = ui
        self.logic = logic
        #     self.connect_signals()

        # def connect_signals(self):
        #     self.ui.update_widget_btn.clicked.connect(self.logic.some_method)