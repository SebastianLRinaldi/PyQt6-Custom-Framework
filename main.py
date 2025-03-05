import sys
from PyQt6.QtWidgets import QApplication
from application_draft.FrontEnd.presentations.myFirstWindow.myFirstWindowLayout import *



def main():
    app = QApplication(sys.argv)
    my_first_page()
    
    return app.exec()  
    
if __name__ == "__main__":
    main()