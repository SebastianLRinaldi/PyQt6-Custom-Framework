from application.apps.myThirdWindow.myThirdWindowLayout import My_Third_Page

class ThirdPageLogic:
    def __init__(self, ui: My_Third_Page):
        self.ui: My_Third_Page = ui

    def update_label(self, text: str):
        self.ui.label.setText(text)