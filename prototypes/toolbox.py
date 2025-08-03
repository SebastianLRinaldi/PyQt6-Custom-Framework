"""
Basic Example
"""
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QToolBox, QLabel
# import sys

# app = QApplication(sys.argv)

# window = QWidget()
# window.setWindowTitle("ToolBox Example")
# layout = QVBoxLayout()

# toolbox = QToolBox()
# toolbox.addItem(QLabel("General Settings..."), "General")
# toolbox.addItem(QLabel("Advanced Options..."), "Advanced")
# toolbox.addItem(QLabel("Other Stuff..."), "Other")

# layout.addWidget(toolbox)
# window.setLayout(layout)
# window.resize(300, 200)
# window.show()
# sys.exit(app.exec())



from PyQt6.QtWidgets import (
    QApplication, QWidget, QToolBox, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QComboBox, QLineEdit, QTextEdit
)
import sys

class ToolBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QToolBox Example")
        self.resize(400, 300)
        layout = QVBoxLayout()

        self.toolbox = QToolBox()

        # Panel 1: Form
        form_widget = QWidget()
        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Name:"))
        form_layout.addWidget(QLineEdit())
        form_layout.addWidget(QLabel("Email:"))
        form_layout.addWidget(QLineEdit())
        form_widget.setLayout(form_layout)
        self.toolbox.addItem(form_widget, "User Info")

        # Panel 2: Settings
        settings_widget = QWidget()
        settings_layout = QVBoxLayout()
        combo = QComboBox()
        combo.addItems(["Light", "Dark", "System"])
        settings_layout.addWidget(QLabel("Theme"))
        settings_layout.addWidget(combo)
        settings_widget.setLayout(settings_layout)
        self.toolbox.addItem(settings_widget, "Settings")

        # Panel 3: Logs
        log_widget = QWidget()
        log_layout = QVBoxLayout()
        self.logs = QTextEdit()
        self.logs.setReadOnly(True)
        log_layout.addWidget(self.logs)
        refresh_button = QPushButton("Refresh Logs")
        refresh_button.clicked.connect(self.update_logs)
        log_layout.addWidget(refresh_button)
        log_widget.setLayout(log_layout)
        self.toolbox.addItem(log_widget, "Logs")

        layout.addWidget(self.toolbox)
        self.setLayout(layout)

    def update_logs(self):
        self.logs.setPlainText("Log Entry 1\nLog Entry 2\nLog Entry 3\n[Updated]")

app = QApplication(sys.argv)
window = ToolBoxDemo()
window.show()
sys.exit(app.exec())

