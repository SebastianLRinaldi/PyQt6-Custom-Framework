"""
Basic Example
"""
# from PyQt6.QtWidgets import QApplication, QMainWindow, QDockWidget, QLabel, QTextEdit
# from PyQt6.QtCore import Qt
# import sys

# app = QApplication(sys.argv)

# main_window = QMainWindow()
# main_window.setWindowTitle("Dock Widget Example")
# main_window.resize(600, 400)

# # Central widget
# main_window.setCentralWidget(QTextEdit("Main Content"))

# # Dock widget
# dock = QDockWidget("Side Panel")
# dock.setWidget(QLabel("Docked content here"))
# main_window.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

# main_window.show()
# sys.exit(app.exec())

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QDockWidget, QTextEdit, QListWidget, QPushButton,
    QVBoxLayout, QWidget, QLabel
)
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QDockWidget Example")
        self.resize(800, 600)

        # Central widget
        self.editor = QTextEdit("Main Editor")
        self.setCentralWidget(self.editor)

        # File list dock
        self.file_dock = QDockWidget("Files", self)
        self.file_list = QListWidget()
        self.file_list.addItems(["file1.txt", "file2.txt", "script.py"])
        self.file_list.currentTextChanged.connect(self.load_file)
        self.file_dock.setWidget(self.file_list)
        self.file_dock.setFloating(False)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.file_dock)

        # Inspector dock
        self.inspector_dock = QDockWidget("Inspector", self)
        self.inspector_widget = QLabel("Select a file to view info")
        self.inspector_dock.setWidget(self.inspector_widget)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.inspector_dock)

        # Tools dock (can float)
        self.tools_dock = QDockWidget("Tools", self)
        tools_container = QWidget()
        tools_layout = QVBoxLayout()
        tools_layout.addWidget(QPushButton("Run"))
        tools_layout.addWidget(QPushButton("Build"))
        tools_container.setLayout(tools_layout)
        self.tools_dock.setWidget(tools_container)
        self.tools_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable | QDockWidget.DockWidgetFeature.DockWidgetFloatable)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.tools_dock)

    def load_file(self, filename):
        self.editor.setPlainText(f"Loaded content from: {filename}")
        self.inspector_widget.setText(f"Inspecting: {filename}\nSize: ?? KB\nModified: Today")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
