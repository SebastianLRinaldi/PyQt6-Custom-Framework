from FrontEnd.A_frameworks.gridLayoutFrameworks import *
from FrontEnd.A_frameworks.widgetFrameworks import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Progressive FlashCards")
        self.resize(1000, 600)
        self.setup_stylesheets()
    

    def add_widgets_to_window(self, *widgets):
        grid_layout = GridLayout(*widgets, window=self.window)
        central_widget = Widget(grid_layout)
        self.setCentralWidget(central_widget)

    def show_window(self):
        self.show()
        
    def setup_stylesheets(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a0d1c;
            }
        """)

