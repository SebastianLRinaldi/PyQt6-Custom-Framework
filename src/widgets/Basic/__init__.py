from .Layout import Layout
from .Functions import Logic
from .Connections import Connections

class Composite():
    def __init__(self):
        super().__init__()
        self.layout = Layout()
        self.logic = Logic(self.layout)
        self.connection = Connections(self.layout, self.logic)



    def closeEvent(self, event):
        self.layout.save_settings()
        super().closeEvent(event)