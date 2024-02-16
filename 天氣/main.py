import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_untitled

 
#demo
def buttonClicked(girl):
    girl.textBrowser.append("hello world! This is my first pyQt5 program.")
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_untitled.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(lambda:buttonClicked(ui))
    MainWindow.show()
    sys.exit(app.exec_())