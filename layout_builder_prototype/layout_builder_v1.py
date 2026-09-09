import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout,
    QSplitter, QTabWidget, QPushButton, QListWidget
)
from PyQt6.QtCore import Qt


def build_layout(data, widgets):
    if isinstance(data, str):
        return widgets[data]

    if isinstance(data, list):
        layout = QHBoxLayout()
        for item in data:
            child = build_layout(item, widgets)
            layout.addWidget(_as_widget(child))
        return layout

    if isinstance(data, dict):
        if "splitter" in data:
            info = data["splitter"]
            splitter = QSplitter(Qt.Orientation.Vertical if info.get("orientation") == "vertical" else Qt.Orientation.Horizontal)
            for item in info["children"]:
                child = build_layout(item, widgets)
                splitter.addWidget(_as_widget(child))
            return splitter

        if "tabs" in data:
            tabs = QTabWidget()
            for idx, item in enumerate(data["tabs"]["children"]):
                child = build_layout(item, widgets)
                tabs.addTab(_as_widget(child), f"Tab {idx+1}")
            return tabs

        if "grid" in data:
            layout = QGridLayout()
            children = data["grid"]["children"]
            rows = data["grid"].get("rows", 1)
            cols = data["grid"].get("columns", len(children))
            for i, item in enumerate(children):
                child = build_layout(item, widgets)
                layout.addWidget(_as_widget(child), i // cols, i % cols)
            return layout

        if "stacked" in data:
            layout = QStackedLayout()
            for item in data["stacked"]["children"]:
                layout.addWidget(_as_widget(build_layout(item, widgets)))
            return layout

    # default vertical
    layout = QVBoxLayout()
    for item in data:
        layout.addWidget(_as_widget(build_layout(item, widgets)))
    return layout


def _as_widget(item):
    if isinstance(item, QWidget):
        return item
    container = QWidget()
    container.setLayout(item)
    return container


def main():
    app = QApplication(sys.argv)

    widgets = {
        "grammar_list": QListWidget(),
        "noun_list": QListWidget(),
        "verb_list": QListWidget(),
        "sync_btn": QPushButton("Sync"),
        "randomize_btn": QPushButton("Randomize"),
    }

    # layout_data = {
    #     "splitter": {
    #         "orientation": "vertical",
    #         "children": [
    #             ["grammar_list", "noun_list"],
    #             {
    #                 "tabs": {
    #                     "children": [
    #                         ["sync_btn", "randomize_btn"],
    #                         ["verb_list"]
    #                     ]
    #                 }
    #             }
    #         ]
    #     }
    # }

    layout_data = [
        "grammar_list",
        {
        "splitter": {
            "orientation": "horizontal",
            "children": [
                "noun_list",
                {
                    "tabs": {
                        "children": [
                            ["sync_btn", "randomize_btn"],  # horizontal in tab 1
                            "randomize_btn",
                        ]
                    }
                },
            ],
        }
        },
        {

        }
    ]

    window = QWidget()

    result = build_layout(layout_data, widgets)

    layout = QVBoxLayout()
    layout.addWidget(result) if isinstance(result, QWidget) else layout.addLayout(result)
    window.setLayout(layout)



    window.resize(600, 400)
    window.setWindowTitle("Simplified Layout Demo")
    window.show()




    sys.exit(app.exec())


if __name__ == "__main__":
    main()



layout_data = [
            "grammar_list",
            "noun_list",
            ["sync_btn", "randomize_btn"],  # horizontal
        ]


layout_data = {
            "splitter": {
                "orientation": "vertical",
                "children": [
                    "label",
                    {
                        "tabs": {
                            "children": [
                                {
                                    "splitter": {
                                        "orientation": "horizontal",
                                        "children": [
                                            "list1",
                                            {
                                                "tabs": {
                                                    "children": [
                                                        {
                                                            "grid": {
                                                                "rows": 2,
                                                                "columns": 2,
                                                                "children": [
                                                                    "grid_label1",
                                                                    "grid_label2",
                                                                    "grid_label3",
                                                                    {
                                                                        "stacked": {
                                                                            "children": [
                                                                                "stacked1",
                                                                                "stacked2"
                                                                            ]
                                                                        }
                                                                    }
                                                                ]
                                                            }
                                                        },
                                                        {
                                                            "splitter": {
                                                                "orientation": "vertical",
                                                                "children": [
                                                                    ["button1", "button2"],
                                                                    {
                                                                        "tabs": {
                                                                            "children": [
                                                                                ["label2", "list2"],
                                                                                ["button3", "button4"]
                                                                            ]
                                                                        }
                                                                    }
                                                                ]
                                                            }
                                                        }
                                                    ]
                                                }
                                            }
                                        ]
                                    }
                                },
                                "deep_label"
                            ]
                        }
                    }
                ]
            }
        }