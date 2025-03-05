import sys
from PyQt6.QtWidgets import QApplication
from application.FrontEnd.presentations.mySecondWindow.mySecondWindowLayout import *
from application.FrontEnd.presentations.myFirstWindow.myFirstWindowLayout import *


def main():
    app = QApplication(sys.argv)
    my_first_page()
    my_second_page()
    
    return app.exec()  
    
if __name__ == "__main__":
    main()