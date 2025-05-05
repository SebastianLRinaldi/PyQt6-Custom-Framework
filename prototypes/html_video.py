
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys
import os

app = QApplication(sys.argv)

view = QWebEngineView()
html_path = os.path.abspath("video.html")
view.setUrl(QUrl.fromLocalFile(html_path))

window = QMainWindow()
window.setCentralWidget(view)
window.resize(800, 600)
window.show()

sys.exit(app.exec())
