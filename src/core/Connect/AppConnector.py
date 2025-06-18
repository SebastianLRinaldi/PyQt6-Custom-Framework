from typing import Dict, TypedDict
from src.apps.BasicApp.basicFunctions import*
from src.apps.SecondApp.mySecondWindowFunctions import*
from src.apps.WebApp.webFunctions import*

class LogicDict(TypedDict):
    Basic: BasicLogic
    Second:SecondLogic
    Web: WebLogic

class AppConnector:
    def __init__(self, logic: LogicDict):
        self.logic = logic

        # self.logic["Basic"].ui.update_widget_btn.clicked.connect(
        #     self.logic["Second"].update_widget
        # )

        # self.logic["Basic"].ui.reset_widget_btn.clicked.connect(
        #     lambda: self.logic["Second"].ui.name_label.setText("Updated Another Way")
        # )
        