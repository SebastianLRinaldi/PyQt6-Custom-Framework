from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from typing import Dict, TypeVar, Union


# class LayoutManager(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My Progressive FlashCards")
#         self.resize(1000, 600)
#         self.setup_stylesheets()
#         self.widget_layout = None

#     def add_widgets_to_window(self, *widgets, setlayout:str=None):
#         if setlayout == "V" or setlayout == None:
#             self.widget_layout = QVBoxLayout()
#             for index, widget in enumerate(widgets):
#                 self.widget_layout.addWidget(widget)
#             self.setLayout(self.widget_layout)

#         elif setlayout == "H":
#             self.widget_layout = QHBoxLayout()
#             for index, widget in enumerate(widgets):
#                 self.widget_layout.addWidget(widget)
#             self.setLayout(self.widget_layout)
            
#         return self

#     def show_window(self):
#         self.show()

#     def setup_stylesheets(self):
#         self.setStyleSheet("""
#             QMainWindow {
#                 background-color: #1a0d1c;
#             }
#             QLabel {
#                 background-color: #AAAAAA;
#             }
#         """)


from typing import Literal, Union
Orientation = Literal["horizontal", "vertical"]
LayoutType = Literal["group", "splitter", "tabs", "grid", "stacked"]

class LayoutManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App UI")
        self.resize(1000, 600)
        self.setup_stylesheets()
        # self.widget_layout = None

    def setup_stylesheets(self):
        self.setStyleSheet("""
            QLabel { background-color: #AAAAAA; }
        """)

    def _as_widget(self, item):
        if isinstance(item, QWidget):
            return item
        if isinstance(item, QLayout):
            wrapper = QWidget()
            wrapper.setLayout(item)
            return wrapper
        raise TypeError(f"Unsupported item type: {type(item)}")

    def build_layout(self, data):
        if isinstance(data, str):
            return getattr(self, data)

        if isinstance(data, list):
            # default layout if bare list, say vertical
            layout = QVBoxLayout()
            for item in data:
                layout.addWidget(self._as_widget(self.build_layout(item)))
            return layout

        if isinstance(data, dict):
            if "group" in data:
                info = data.get("group", {})
                orient = info.get("orientation", "vertical")
                children = info.get("children", [])
                layout = QVBoxLayout() if orient == "vertical" else QHBoxLayout()
                for item in children:
                    layout.addWidget(self._as_widget(self.build_layout(item)))
                return layout

            if "splitter" in data:
                info = data["splitter"]
                splitter = QSplitter(
                    Qt.Orientation.Vertical if info.get("orientation") == "vertical"
                    else Qt.Orientation.Horizontal
                )
                for item in info["children"]:
                    splitter.addWidget(self._as_widget(self.build_layout(item)))
                return splitter

            if "tabs" in data:
                tabs = QTabWidget()
                for idx, item in enumerate(data["tabs"]["children"]):
                    tabs.addTab(self._as_widget(self.build_layout(item)), f"Tab {idx + 1}")
                return tabs

            if "grid" in data:
                layout = QGridLayout()
                children = data["grid"]["children"]
                rows = data["grid"].get("rows", 1)
                cols = data["grid"].get("columns", len(children))
                for i, item in enumerate(children):
                    layout.addWidget(
                        self._as_widget(self.build_layout(item)),
                        i // cols, i % cols
                    )
                return layout

            if "stacked" in data:
                layout = QStackedLayout()
                for item in data["stacked"]["children"]:
                    layout.addWidget(self._as_widget(self.build_layout(item)))
                return layout

        layout = QVBoxLayout()
        for item in data:
            layout.addWidget(self._as_widget(self.build_layout(item)))
        return layout

    def apply_layout(self, layout_data):
        result = self.build_layout(layout_data)
        layout = QVBoxLayout()
        layout.addWidget(self._as_widget(result))
        self.setLayout(layout)

    def group(self, orientation: Orientation, children:list):
        return {
            "group": {
                "orientation": orientation,
                "children": children
            }
        }

    def splitter(self, orientation: Orientation, children:list):
        return {
            "splitter": {
                "orientation": orientation,
                "children": children
            }
        }

    def tabs(self, children:list):
        return {
            "tabs": {
                "children": children
            }
        }

    def grid(self, children:list, rows=1, columns=None):
        return {
            "grid": {
                "children": children,
                "rows": rows,
                "columns": columns or len(children)
            }
        }

    def stacked(self, children:list):
        return {
            "stacked": {
                "children": children
            }
        }



    def show_window(self):
        self.show()

    def setup_stylesheets(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a0d1c;
            }
            QLabel {
                background-color: #AAAAAA;
            }
        """)
