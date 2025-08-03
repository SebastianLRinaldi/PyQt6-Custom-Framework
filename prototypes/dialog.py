from PyQt6.QtWidgets import (
    QApplication, QDialog, QDialogButtonBox, QVBoxLayout, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt, QTimer
import sys

class FullFeatureDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("All QDialogButtonBox Buttons & Roles Demo")

        layout = QVBoxLayout(self)

        # Combine all StandardButtons using bitwise OR
        all_buttons = (
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Save |
            QDialogButtonBox.StandardButton.SaveAll |
            QDialogButtonBox.StandardButton.Open |
            QDialogButtonBox.StandardButton.Yes |
            QDialogButtonBox.StandardButton.YesToAll |
            QDialogButtonBox.StandardButton.No |
            QDialogButtonBox.StandardButton.NoToAll |
            QDialogButtonBox.StandardButton.Abort |
            QDialogButtonBox.StandardButton.Retry |
            QDialogButtonBox.StandardButton.Ignore |
            QDialogButtonBox.StandardButton.Close |
            QDialogButtonBox.StandardButton.Cancel |
            QDialogButtonBox.StandardButton.Discard |
            QDialogButtonBox.StandardButton.Help |
            QDialogButtonBox.StandardButton.Apply |
            QDialogButtonBox.StandardButton.Reset |
            QDialogButtonBox.StandardButton.RestoreDefaults
        )

        self.button_box = QDialogButtonBox(all_buttons)
        layout.addWidget(self.button_box)

        # Connect signals
        self.button_box.accepted.connect(lambda: print("accepted signal"))
        self.button_box.rejected.connect(lambda: print("rejected signal"))
        self.button_box.helpRequested.connect(self.on_help)
        self.button_box.clicked.connect(self.on_clicked)

        # Print info for each button
        for btn in self.button_box.buttons():
            std_btn = self.button_box.standardButton(btn)
            role = self.button_box.buttonRole(btn)
            print(f"Button: '{btn.text()}' | StandardButton: {std_btn} | Role: {role}")

        # Remove "Discard" button after 2 seconds
        QTimer.singleShot(2000, self.remove_discard)

    def on_help(self):
        print("Help button clicked")

    def on_clicked(self, btn):
        print(f"Clicked button: '{btn.text()}', Role: {self.button_box.buttonRole(btn)}")

    def remove_discard(self):
        discard_btn = self.button_box.button(QDialogButtonBox.StandardButton.Discard)
        if discard_btn:
            print("Removing Discard button")
            self.button_box.removeButton(discard_btn)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = FullFeatureDialog()
    dlg.show()
    sys.exit(app.exec())
