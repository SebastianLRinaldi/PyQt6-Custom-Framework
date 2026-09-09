from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtPrintSupport import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWebEngineCore import *
import sys
import os


# os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu --disable-software-rasterizer"
# os.environ["QTWEBENGINE_DISABLE_GPU"] = "1"  # Explicitly disable GPU usage

# Force Qt to use software rendering and no OpenGL at all
# QCoreApplication.setAttribute(Qt.ApplicationAttribute.AA_UseSoftwareOpenGL, on=True)
# QWebEngineView.setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled)
# # Set WebEngine to not use OpenGL
# os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu --no-sandbox"

# # Enable detailed logging for WebEngine
# os.environ["QT_LOGGING_RULES"] = "qt.webenginecore.debug=true"
# os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--use-gl=angle --gpu --gpu-launcher --in-process-gpu --ignore-gpu-blacklist --ignore-gpu-blocklist'




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Full Browser Experience")
        self.setGeometry(100, 100, 1200, 800)

        # Set persistent profile
        profile = QWebEngineProfile("Default", self)
        profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies)
        profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.DiskHttpCache)
        profile.setHttpCacheMaximumSize(100 * 1024 * 1024)  # 100 MB
        profile.setPersistentStoragePath("browser_data/storage")
        profile.setCachePath("browser_data/cache")
        profile.setDownloadPath(os.path.abspath("browser_data/downloads"))
        profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) CustomPyQtBrowser")

        # Enable features
        settings = profile.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.FullScreenSupportEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptCanOpenWindows, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.ScreenCaptureEnabled, True)

        # Main browser view
        self.browser = QWebEngineView()
        # self.browser.setPage(profile.newPage())
        self.browser.setUrl(QUrl("https://www.youtube.com/watch?v=K4zHXPQApic"))



        # DevTools view
        self.devtools_view = QWebEngineView()
        self.devtools_view.setWindowTitle("DevTools")
        self.devtools_view.resize(800, 600)
        self.devtools_view.show()

        # Tell the browser to use this dev tools view
        self.browser.page().setDevToolsPage(self.devtools_view.page())

        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.show()

app = QApplication(sys.argv)
window = MainWindow()
app.exec()



# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt6.QtCore import QUrl
# from PyQt6.QtGui import QDesktopServices
# import sys

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Open YouTube in Browser")
#         self.setGeometry(100, 100, 400, 200)

#         button = QPushButton("Watch Video", self)
#         button.clicked.connect(self.open_video)
#         self.setCentralWidget(button)

#     def open_video(self):
#         QDesktopServices.openUrl(QUrl("https://www.youtube.com/watch?v=K4zHXPQApic"))

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
