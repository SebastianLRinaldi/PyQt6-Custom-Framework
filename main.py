import sys
from PyQt5.QtWidgets import QApplication
from application.FrontEnd.presentation.presentation import run_pyqt



def main():
    app = QApplication(sys.argv)
    
    
    run_pyqt()
    
    return app.exec()  
    
if __name__ == "__main__":
    main()