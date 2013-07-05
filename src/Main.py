'''
Created on Jun 25, 2013

@author: bbetts
'''
from src.GUI.ControlMainWindow import ControlMainWindow
from PySide.QtGui import QApplication,QIcon
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("../images/ps2-logo.png"))
    my_app = ControlMainWindow()
    my_app.show()
    sys.exit(app.exec_())