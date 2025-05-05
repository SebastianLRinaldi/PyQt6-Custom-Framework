"""
pyqt6 - v. 6.7 (G)
pyqt6-webengine - v. 6.7 (G)
"""
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtPrintSupport import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWebEngineCore import *
import sys
import os
"""
Test this see if anything changes in terms of speed?
"""
# os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--use-gl=angle --gpu --gpu-launcher --in-process-gpu --ignore-gpu-blacklist --ignore-gpu-blocklist'

# os.environ["QT_OPENGL"] = "angle"
# os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--enable-gpu-rasterization --enable-zero-copy --ignore-gpu-blocklist"


# os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--no-sandbox"
# # os.environ["QT_LOGGING_RULES"] = "qt.webenginecore.debug=true"
# os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu --disable-software-rasterizer"
# os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu --disable-software-rasterizer"
# os.environ["QTWEBENGINE_DISABLE_GPU"] = "1"  # Explicitly disable GPU usage
# QCoreApplication.setAttribute(Qt.ApplicationAttribute.AA_UseSoftwareOpenGL)
# os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--no-sandbox"
# os.environ["QT_LOGGING_RULES"] = "qt.webenginecore.debug=true"
# os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu --disable-software-rasterizer --no-sandbox"


# Add the root directory of your project to the sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from application.FrontEnd.presentations.mySecondWindow.mySecondWindowLayout import *
from application.FrontEnd.presentations.myFirstWindow.myFirstWindowLayout import *



def main():
    app = QApplication(sys.argv)
    my_first_page()
    # my_second_page()
    
    return app.exec()  
    
if __name__ == "__main__":
    main()






# # driver.execute_script("""
# #     var dialog = document.querySelector('div[role="dialog"][aria-labelledby="dialogUpsellTitle"]');
# #     if (dialog) {
# #         dialog.style.display = 'none';
# #     }
# # """)


# # Wait for the dialog to appear
# try:
#     # Wait for the element to be present in the DOM
#     dialog = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="dialog"][aria-labelledby="dialogUpsellTitle"]'))
#     )
    
#     # Once the dialog appears, hide it
#     driver.execute_script("""
#         var dialog = document.querySelector('div[role="dialog"][aria-labelledby="dialogUpsellTitle"]');
#         if (dialog) {
#             dialog.style.display = 'none';  // Hide the dialog
#         }
#     """)
#     print("Dialog hidden.")
# except Exception as e:
#     print(f"Error: {e}")