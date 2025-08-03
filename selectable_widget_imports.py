import sys
import os
from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *


class ImportGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget Import Generator")

        self.widget_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "src", "widgets"))

        self.layout = QVBoxLayout(self)

        # Widget selection list
        self.widget_list = QListWidget()
        self.layout.addWidget(QLabel("Select Widgets:"))
        self.layout.addWidget(self.widget_list)

        # Checkboxes
        self.logic_cb = QCheckBox("Generate Logic")
        self.layout_cb = QCheckBox("Generate Layout")
        self.conn_cb = QCheckBox("Generate Connections")
        for cb in (self.logic_cb, self.layout_cb, self.conn_cb):
            cb.setChecked(True)

        cb_row = QHBoxLayout()
        cb_row.addWidget(self.logic_cb)
        cb_row.addWidget(self.layout_cb)
        cb_row.addWidget(self.conn_cb)
        self.layout.addLayout(cb_row)

        # Grouping mode
        self.group_mode = QButtonGroup(self)
        self.by_widget = QRadioButton("Group by Widget")
        self.by_type = QRadioButton("Group by Type")
        self.by_widget.setChecked(True)
        self.group_mode.addButton(self.by_widget)
        self.group_mode.addButton(self.by_type)

        group_row = QHBoxLayout()
        group_row.addWidget(QLabel("Output Grouping:"))
        group_row.addWidget(self.by_widget)
        group_row.addWidget(self.by_type)
        self.layout.addLayout(group_row)

        # Generate button
        self.gen_btn = QPushButton("Generate Imports")
        self.gen_btn.clicked.connect(self.generate_imports)
        self.layout.addWidget(self.gen_btn)

        # Output box
        self.output_box = QPlainTextEdit()
        self.output_box.setReadOnly(False)
        self.layout.addWidget(QLabel("Generated Output:"))
        self.layout.addWidget(self.output_box)

        self.load_widgets()

    def load_widgets(self):
        for name in os.listdir(self.widget_dir):
            full_path = os.path.join(self.widget_dir, name)
            if os.path.isdir(full_path) and not name.startswith("__"):
                item = QListWidgetItem(name)
                item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
                item.setCheckState(Qt.CheckState.Unchecked)
                self.widget_list.addItem(item)

    def generate_imports(self):
        base_path = "src.widgets"
        selected = []

        for i in range(self.widget_list.count()):
            item = self.widget_list.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                selected.append(item.text())

        logic_imports = []
        layout_imports = []
        conn_imports = []

        logic_vars = []
        layout_vars = []
        conn_vars = []

        for name in selected:
            class_base = name[0].upper() + name[1:]
            var_base = name.lower()

            if self.layout_cb.isChecked():
                layout_imports.append(f"from {base_path}.{name}.Layout import Layout as {class_base}Layout")
                layout_vars.append(f"    {var_base}_ui: {class_base}Layout")

            if self.logic_cb.isChecked():
                logic_imports.append(f"from {base_path}.{name}.Functions import Logic as {class_base}Logic")
                logic_vars.append(f"    {var_base}_logic: {class_base}Logic")

            if self.conn_cb.isChecked():
                conn_imports.append(f"from {base_path}.{name}.Connections import Connections as {class_base}Connections")
                conn_vars.append(f"    {var_base}_connections: {class_base}Connections")

        output = []

        if self.by_widget.isChecked():
            for name in selected:
                class_base = name[0].upper() + name[1:]
                lines = []
                if self.layout_cb.isChecked():
                    lines.append(f"from {base_path}.{name}.Layout import Layout as {class_base}Layout")
                if self.logic_cb.isChecked():
                    lines.append(f"from {base_path}.{name}.Functions import Logic as {class_base}Logic")
                if self.conn_cb.isChecked():
                    lines.append(f"from {base_path}.{name}.Connections import Connections as {class_base}Connections")
                output.extend(lines)
                output.append("")

            if self.layout_cb.isChecked():
                output.append("# Layout Vars")
                output.extend(layout_vars)
                output.append("")
            if self.logic_cb.isChecked():
                output.append("# Logic Vars")
                output.extend(logic_vars)
                output.append("")
            if self.conn_cb.isChecked():
                output.append("# Connections Vars")
                output.extend(conn_vars)
                output.append("")

        else:
            if self.layout_cb.isChecked():
                output.append("# Layout Imports")
                output.extend(layout_imports)
                output.append("")
                output.append("# Layout Vars")
                output.extend(layout_vars)
                output.append("")

            if self.logic_cb.isChecked():
                output.append("# Logic Imports")
                output.extend(logic_imports)
                output.append("")
                output.append("# Logic Vars")
                output.extend(logic_vars)
                output.append("")

            if self.conn_cb.isChecked():
                output.append("# Connection Imports")
                output.extend(conn_imports)
                output.append("")
                output.append("# Connection Vars")
                output.extend(conn_vars)
                output.append("")

        self.output_box.setPlainText("\n".join(output))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImportGenerator()
    window.resize(700, 600)
    window.show()
    sys.exit(app.exec())
