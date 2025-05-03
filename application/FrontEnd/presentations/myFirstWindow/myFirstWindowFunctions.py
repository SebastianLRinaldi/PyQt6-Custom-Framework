from application.FrontEnd.presentations.myFirstWindow.myFirstWindowWidgets import *
# from application.BackEnd.Webview.webviewmanger import *

    
def update_widget() -> None:
    label.setText("Im on 1, I have been updated by 1!")

def reset_widget() -> None:
    label.setText("Im on 1, I have been reset by 1!")
    

def load_url(url):
    eWebPage.setUrl(QUrl(url))

def click_element(xpath):
    print(f"Clicking element with XPath: {xpath}")
    execute_js(xpath, "element.click")

def edit_element(xpath, new_value):
    print(f"Editing element with XPath: {xpath}")
    execute_js(xpath, f'element.value = "{new_value}"')

def disable_element(xpath):
    print(f"Disabling element with XPath: {xpath}")
    # execute_js(xpath, "element.disabled = true;")
    execute_js(xpath, "element.style.display = 'none'", wait=True)
    
def highlight_element(xpath):
    print(f"Highlighting element with XPath: {xpath}")
    # Add style to highlight the element
    highlight_style = """
    element.style.border = "3px solid red";
    element.style.backgroundColor = "yellow";
    """
    execute_js(xpath, highlight_style)
    
def type_text(xpath, text_to_type):
    print(f"Typing into element with XPath: {xpath}")
    # Use JavaScript to simulate typing
    type_script = f"""
    var element = document.evaluate("{xpath}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (element && element.tagName === 'INPUT') {{
        element.value = '{text_to_type}';  // Set the text in the input field
    }}
    """
    execute_js(xpath, type_script)

def get_value_at_xpath(xpath):
    print(f"Getting value from element with XPath: {xpath}")
    # JavaScript to get the value of an element based on XPath
    get_value_script = f"""
    var element = document.evaluate("{xpath}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (element) {{
        return element.value || element.textContent || element.innerText || 'No value found';
    }} else {{
        return 'Element not found';
    }}
    """
    # Use the existing execute_js method to run JavaScript and pass the callback function
    execute_js(xpath, get_value_script)
    
# def observe_xpath_and_execute(xpath, action_script):
#     script = f"""
#     (function() {{
#         const observer = new MutationObserver(function(mutations) {{
#             const el = document.evaluate("{xpath}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
#             if (el) {{
#                 observer.disconnect();
#                 {action_script}
#             }}
#         }});
#         observer.observe(document.body, {{
#             childList: true,
#             subtree: true
#         }});
#     }})();
#     """
#     eWebPage.page().runJavaScript(script) 
    
# def execute_js(xpath, action):
#     """Execute JavaScript on the loaded web page using XPath"""
#     script = f"""
#     var element = document.evaluate("{xpath}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
#     if (element) {{
#         {action};
#     }}
#     """
#     eWebPage.page().runJavaScript(script) 
    
def execute_js(xpath, action_js, wait=False):
    if wait:
        script = f"""
        (function() {{
            const observer = new MutationObserver(function(mutations) {{
                const element = document.evaluate("{xpath}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                if (element) {{
                    observer.disconnect();
                    {action_js}
                }}
            }});
            observer.observe(document.body, {{
                childList: true,
                subtree: true
            }});
        }})();
        """
    else:
        script = f"""
        var element = document.evaluate("{xpath}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (element) {{
            {action_js};
        }}
    """
    eWebPage.page().runJavaScript(script)