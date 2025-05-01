import webview

class WebViewWindowActions:
    @staticmethod
    def on_closed():
        # queue.put("kill_spotify_application")
        print('pywebview window is closed')
    @staticmethod
    def on_loaded():
        print('pywebview Dom is loaded!')
        # queue.put("spotify_application_DOM_loaded")
    @staticmethod
    def on_shown():
        print('pywebview window is shown!')
        # queue.put("spotify_application_webview_on")
        # self.play_btn_spotify_ui_click()
    @staticmethod
    def on_restored():
        print('pywebview window is restored!')
    @staticmethod
    def on_moved(window, x, y):
        print(f"X:{x}, Y:{y}, width:{window.width}, height:{window.height}")

class WebviewDOM:
    def find_element(self, element_id: str):
        try:
            selector = f"{element_id}"
            element = webview.windows[0].dom.get_element(selector)
            if element:
                return element, selector
            else:
                return None, selector
        except Exception as e:
            print(f"Error finding element: {e}")
            # Main window failed to start
            WebviewWindow().change_url(webview.windows[0].get_current_url())
            return None, selector
    
    def mark_element(self, element, color='red'):
        # time.sleep(10)  # Wait for the page to load
        # print(f"Looking for element: {element}")
        selector = f'[{element}]'
        element = webview.windows[0].dom.get_element(selector)
        
        if element:
            # print("Found element:", element.tag)
            # Draw a red box around the element
            js_code = f'''
            var element = document.querySelector('{selector}');
            if (element) {{
                element.style.border = "2px solid {color}";
                element.style.boxShadow = "0 0 10px {color}";
                console.log("{color} box drawn around the element");
            }} else {{
                console.log('Element not found');
            }}
            '''
            # Execute the JavaScript code
            result = webview.windows[0].evaluate_js(js_code)
        else:
            print("Element not found")

    def evaluate_js(self, js_code):
        # Implement JavaScript evaluation logic
        webview.windows[0].evaluate_js(js_code)
        pass

    def read_cookies(self):
        cookies = webview.windows[0].get_cookies()
        for c in cookies:
            print(c.output())

class WebviewWindow:
    def __init__(self):
        pass

    def blank_logic(self, window):
        print(f"Start: {window}")
        
    def change_url(self, url):
        webview.windows[0].load_url(url)
        
    def start_webview(self, backend_logic, window, menuitems=[]):
        webview.start(backend_logic, window, menu=menuitems, user_agent="MMozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", private_mode=False, debug=False)
        
    def set_and_start_window(self, backend_logic, url):
        self.window = webview.create_window('My Webview', url, x=508, y=840-135, width=724, height=135, background_color='#00FFFF', transparent=False, minimized=True,  shadow=False, on_top=False, frameless=True, easy_drag=True)
        webview.windows[0].events.closed += WebViewWindowActions.on_closed
        webview.windows[0].events.loaded += WebViewWindowActions.on_loaded # When DOM is loaded
        webview.windows[0].events.shown += WebViewWindowActions.on_shown # When webview window is loaded
        webview.windows[0].events.restored += WebViewWindowActions.on_restored
        # webview.windows[0].events.moved += WebViewWindowActions.on_moved

        # Start the webview on the main thread and run back_endlogic in another thread
        # his will launch a separate thread and is identical to starting a thread by hand.
        self.start_webview(backend_logic, self.window)