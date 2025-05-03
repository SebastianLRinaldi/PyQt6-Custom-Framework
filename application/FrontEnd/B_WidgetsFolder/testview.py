# import sys
# import json
# import multiprocessing
# import webview
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit
# from queue import Empty as QueueEmpty

# class Api:
#     def __init__(self, queue):
#         self.queue = queue

#     def send_url(self, url):
#         self.queue.put(json.dumps({'url': url}))

# def start_webview(queue):
#     api = Api(queue)
#     window = webview.create_window("WebView Window", "https://example.com", js_api=api)

#     def on_loaded():
#         js = "window.pywebview.api.send_url(window.location.href);"
#         webview.windows[0].evaluate_js(js)

#     webview.start(on_loaded, debug=True, gui='qt')

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.queue = multiprocessing.Queue()
#         self.webview_process = multiprocessing.Process(target=start_webview, args=(self.queue,))
#         self.webview_process.start()

#         self.setWindowTitle("PyQt6 Webview Controller")
#         self.resize(400, 200)

#         self.button = QPushButton("Get URL from WebView")
#         self.output = QTextEdit()
#         self.output.setReadOnly(True)

#         layout = QVBoxLayout()
#         layout.addWidget(self.button)
#         layout.addWidget(self.output)
#         self.setLayout(layout)

#         self.button.clicked.connect(self.fetch_url)

#     def fetch_url(self):
#         try:
#             result = self.queue.get(timeout=3)
#             data = json.loads(result)
#             self.output.append(f"Current URL: {data['url']}")
#         except QueueEmpty:
#             self.output.append("No response received from webview (timed out).")
#         except json.JSONDecodeError:
#             self.output.append("Webview returned invalid JSON.")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())







# import sys
# import json
# import time
# import multiprocessing
# import webview
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit
# from queue import Empty

# def start_webview(queue):
#     window = webview.create_window("WebView Window", "https://example.com")

#     def get_url():
#         current_url = webview.windows[0].get_current_url() #window.evaluate_js('window.location.href')
#         if current_url:  # Ensure we got a string
#             queue.put(json.dumps({'url': current_url}))
#         else:
#             queue.put(json.dumps({'url': None}))


#     def on_loaded():
#         # Wait for command
#         while True:
#             if not queue.empty():
#                 request = queue.get()
#                 if request == 'get_url':
#                     get_url()
#             time.sleep(0.1)

#     webview.start(on_loaded)


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.queue = multiprocessing.Queue()
#         self.webview_process = multiprocessing.Process(target=start_webview, args=(self.queue,))
#         self.webview_process.start()

#         self.setWindowTitle("PyQt6 Webview Controller")
#         self.resize(400, 200)

#         self.button = QPushButton("Get URL from WebView")
#         self.output = QTextEdit()
#         self.output.setReadOnly(True)

#         layout = QVBoxLayout()
#         layout.addWidget(self.button)
#         layout.addWidget(self.output)
#         self.setLayout(layout)

#         self.button.clicked.connect(self.fetch_url)

#     def fetch_url(self):
#         self.queue.put('get_url')
#         time.sleep(1)  # Give it time to respond

#         try:
#             result = self.queue.get(timeout=3)
#             data = json.loads(result)
#             print(f"Current URL: {data['url']}")
#         except Empty:
#             print("No response received from webview (timed out).")
#         except json.JSONDecodeError:
#             print("Webview returned invalid JSON.")


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())


import webview
import multiprocessing
import time
import json

def start_webview(queue):
    window = webview.create_window("WebView Window", "https://example.com")

    def get_url():
        current_url = window.evaluate_js('window.location.href')
        if current_url:  # Ensure we got a string
            queue.put(json.dumps({'url': current_url}))
        else:
            queue.put(json.dumps({'url': None}))

    def on_loaded():
        # Wait for command
        while True:
            # if not queue.empty():
            request = queue.get()
            if request == 'get_url':
                get_url()
                break
            time.sleep(0.1)

    webview.start(on_loaded)

def main():
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=start_webview, args=(queue,))
    process.start()

    time.sleep(5)  # Give the webview time to start and load
    while True:
        queue.put('get_url')
        time.sleep(1)  # Give it time to respond

        if not queue.empty():
            result = queue.get()
            data = json.loads(result)
            print(f"Current URL: {data['url']}")
        else:
            print("No response received from webview.")

    # process.terminate()

if __name__ == '__main__':
    main()
