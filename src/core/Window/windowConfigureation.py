from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from src.core.Grouper.SpliterGroupConfiguration import *
from src.core.Grouper.TabGroupConfigureation import *
from src.core.Grouper.widgetGroupFrameworks import *

from typing import Literal

Orientation = Literal["horizontal", "vertical"]
LayoutType = Literal["group", "splitter", "tabs", "grid", "stacked"]

class LayoutManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App UI")
        self.resize(1000, 600)
        self.setup_stylesheets()
        self.widget_layout = None

    def build_layout(self, data) -> QWidget | QLayout:
        if isinstance(data, str):
            return getattr(self, data)  # user widgets expected here

        if isinstance(data, list):
            layout = QVBoxLayout()
            for item in data:
                w = self.build_layout(item)
                if isinstance(w, QWidget):
                    layout.addWidget(w)
                else:
                    layout.addLayout(w)
            return layout

        if isinstance(data, dict):
            if "group" in data:
                info = data["group"]
                orient = info.get("orientation", "vertical")
                children = info.get("children", [])

                layout = QVBoxLayout() if orient == "vertical" else QHBoxLayout()
                for item in children:
                    w = self.build_layout(item)
                    if isinstance(w, QWidget):
                        layout.addWidget(w)
                    else:
                        layout.addLayout(w)

                return layout

            if "box" in data:
                info = data["box"]
                title = info.get("title", "")
                orient = info.get("orientation", "vertical")
                children = info.get("children", [])
                
                groupbox = QGroupBox(title) 
                layout = QVBoxLayout() if orient == "vertical" else QHBoxLayout()
                for item in children:
                    w = self.build_layout(item)
                    if isinstance(w, QWidget):
                        layout.addWidget(w,  stretch=1)
                    else:
                        container = QWidget()
                        container.setLayout(w)
                        layout.addWidget(container, stretch=1)

                # layout.setContentsMargins(0, 0, 0, 0)
                # layout.setSpacing(0)
                # groupbox.setFlat(True)  # Optional: removes border if you want
                # groupbox.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

                groupbox.setLayout(layout)

                return groupbox

            if "splitter" in data:
                info = data["splitter"]
                orient = Qt.Orientation.Vertical if info.get("orientation") == "vertical" else Qt.Orientation.Horizontal
                splitter = QSplitter(orient)
                for item in info["children"]:
                    w = self.build_layout(item)
                    if isinstance(w, QWidget):
                        splitter.addWidget(w)
                    else:
                        container = QWidget()
                        container.setLayout(w)
                        splitter.addWidget(container)

                return splitter

            if "tabs" in data:
                info = data["tabs"]
                tabs = QTabWidget()
                for idx, item in enumerate(info["children"]):
                    w = self.build_layout(item)
                    if isinstance(w, QWidget):
                        tabs.addTab(w, f"Tab {idx + 1}")
                    else:
                        container = QWidget()
                        container.setLayout(w)
                        tabs.addTab(container, f"Tab {idx + 1}")

                return tabs

            if "grid" in data:
                info = data["grid"]
                layout = QGridLayout()
                children = info["children"]
                rows = info.get("rows", 1)
                cols = info.get("columns", len(children))
                for i, item in enumerate(children):
                    w = self.build_layout(item)
                    if isinstance(w, QWidget):
                        layout.addWidget(w, i // cols, i % cols)
                    else:
                        container = QWidget()
                        container.setLayout(w)
                        layout.addWidget(container, i // cols, i % cols)
                return layout

            if "stacked" in data:
                info = data["stacked"]
                layout = QStackedLayout()
                for item in info["children"]:
                    w = self.build_layout(item)
                    if isinstance(w, QWidget):
                        layout.addWidget(w)
                    else:
                        container = QWidget()
                        container.setLayout(w)
                        layout.addWidget(container)
                container = QWidget()
                container.setLayout(layout)
                return container

        raise TypeError("Invalid layout data")

    # def apply_layout(self, layout_data):
    #     layout_or_widget = self.build_layout(layout_data)
    #     if isinstance(layout_or_widget, QWidget):
    #         main_layout = QVBoxLayout()
    #         main_layout.addWidget(layout_or_widget)
    #         self.setLayout(main_layout)
            
    #     else:
    #         self.setLayout(layout_or_widget)


    def apply_layout(self, layout_data):
        layout_or_widget = self.build_layout(layout_data)

        if isinstance(layout_or_widget, QWidget):
            # If it's already a widget with its own layout, set it as central widget
            self.setLayout(QVBoxLayout())  # force minimal root layout if needed
            self.layout().addWidget(layout_or_widget)
            # self.layout().setContentsMargins(0, 0, 0, 0)
            # self.layout().setSpacing(0)
        else:
            layout_or_widget.setContentsMargins(0, 0, 0, 0)
            # layout_or_widget.setSpacing(0)
            self.setLayout(layout_or_widget)

    def group(self, orientation: Orientation, children:list):
        return {
            "group": {
                "orientation": orientation,
                "children": children
            }
        }

    def box(self, orientation: Orientation, children:list):
        return {
            "box": {
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
    def print_margins_recursive(self, widget: QWidget):
        layout = widget.layout()
        if layout:
            margins = layout.contentsMargins()
            print(f"{widget.__class__.__name__} margins:", margins.left(), margins.top(), margins.right(), margins.bottom(), "spacing:", layout.spacing())
            for i in range(layout.count()):
                item = layout.itemAt(i)
                child = item.widget()
                if child:
                    self.print_margins_recursive(child)