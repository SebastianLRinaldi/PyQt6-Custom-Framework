from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import (
    QWebEngineProfile,
    QWebEnginePage,
    QWebEngineScript,
    QWebEngineUrlRequestInterceptor,
)
from PyQt6.QtCore import QUrl
import sys


# 🔧 1. Ad Blocker / Request Interceptor
class AdBlockInterceptor(QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        if any(x in url for x in ["ads", "tracker", "doubleclick", "googlesyndication", "amazon-adsystem"]):
            info.block(True)


# 🔧 2. Main App Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stealth Browser")

        # 🌐 Profile Setup
        self.profile = QWebEngineProfile("AdFree", self)
        self.profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.NoCache)
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.NoPersistentCookies)
        self.profile.setSpellCheckEnabled(False)
        self.profile.setPushServiceEnabled(False)
        self.profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36")
        self.profile.setUrlRequestInterceptor(AdBlockInterceptor())

        # 🧠 JavaScript Injection to Clean Ads/PW
        script = QWebEngineScript()
        script.setSourceCode("""
            const nuke = () => {
                const adSelectors = ['[id*="ad"]', '[class*="ad"]', '[id*="sponsor"]', '[class*="sponsor"]', '[class*="banner"]'];
                adSelectors.forEach(sel => document.querySelectorAll(sel).forEach(el => el.remove()));

                // Paywall common tricks
                let html = document.documentElement;
                html.style.overflow = 'auto';
                document.querySelectorAll('[style*="overflow"]').forEach(el => el.style.overflow = 'auto');

                // Stop Beacon tracking
                if (navigator.sendBeacon) navigator.sendBeacon = () => false;
            };
            new MutationObserver(nuke).observe(document.body, { childList: true, subtree: true });
            window.addEventListener('DOMContentLoaded', nuke);
            nuke();
        """)
        script.setInjectionPoint(QWebEngineScript.InjectionPoint.DocumentReady)
        script.setWorldId(QWebEngineScript.ScriptWorldId.MainWorld)
        script.setRunsOnSubFrames(True)
        self.profile.scripts().insert(script)

        # 🌐 Web Page & View
        self.page = QWebEnginePage(self.profile, self)
        self.view = QWebEngineView()
        self.view.setPage(self.page)
        self.page.load(QUrl("https://www.youtube.com"))  # Replace with your target URL

        # 🖼️ Layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.view)
        self.setCentralWidget(central_widget)


# 🧠 Run App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(1200, 800)
    window.show()
    sys.exit(app.exec())
