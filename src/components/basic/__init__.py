from .layout import Layout
from .logic import Logic
from .connections import Connections

class Component():
    def __init__(self):
        super().__init__()
        self.layout = Layout.Layout()
        self.logic = Logic.Logic(self.layout)
        self.connections = Connections.Connections(self.layout, self.logic)
