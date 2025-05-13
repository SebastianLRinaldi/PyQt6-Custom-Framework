from typing import Dict, TypedDict
from application.apps.myFirstWindow.myFirstWindowFunctions import*
from application.apps.myThirdWindow.myThirdWindowFunctions import*
# This is your scalable logic dict
class LogicDict(TypedDict):
    first: FirstPageLogic
    third: ThirdPageLogic
    # Add more entries here for new pages as needed


class PageController:
    def __init__(self, logic: LogicDict):
        self.logic = logic
        self.connect_signals()

    def connect_signals(self):
        # Dynamically connects first page's signal to second page's method
        self.logic["first"].ui.update_widget_btn.clicked.connect(
            lambda: self.logic["third"].update_label("Updated from First Page")
        )