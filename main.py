import sys
from PyQt6.QtWidgets import QApplication
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