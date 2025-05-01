from application.FrontEnd.presentations.myFirstWindow.myFirstWindowWidgets import *
from application.BackEnd.Webview.webviewmanger import *

def on_click() -> None:
    pass
    
def update_label() -> None:
    label.setText("Im on 1, I have been updated by 1!")

def reset_label() -> None:
    label.setText("Im on 1, I have been reset by 1!")

import multiprocessing
def start_page() -> None:
    # Make a new terminal and run a python file 
    # script_path = r'main_webview.py'    
    # process = subprocess.Popen(["start", "cmd", "/k", f"python {script_path}"], shell=True)
    
    process = multiprocessing.Process(target=run_script_2)
    process.start()

def run_script_2():
    
    webview_window = WebviewWindow()
    webview_window.set_and_start_window(None, "https://example.com")
    
    # Start the second script in a seperate main as a separate process using subprocess
    # script_path = r'F:\_Small\344 School Python\PYQTFRAMEWORK\main_webview.py'
    # subprocess.Popen(["python", script_path])


# This would be where we connect to backend webview manger?  
def embed_page() -> None:
    hwnd = win32gui.FindWindow(None, "My Webview")
    eWebPage.embed_window(hwnd)
    