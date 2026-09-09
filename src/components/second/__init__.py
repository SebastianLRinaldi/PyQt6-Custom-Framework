from .layout import Layout
from .logic import Logic
from .connections import Connections

class CompositeWidget():
    def __init__(self):
        super().__init__()
        self.layout = Layout()
        self.logic = Logic(self.layout)
        self.connections = Connections(self.layout, self.logic)