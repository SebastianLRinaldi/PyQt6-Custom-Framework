from application.BackEnd.Webview.webviewmanger import *
def get_webpage() -> None:

    webview_window = WebviewWindow()
    webview_window.set_and_start_window(None, "https://example.com")

    
get_webpage()
