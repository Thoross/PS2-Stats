'''
PS2-Stats : Python module for PlanetSide 2 Stat tracking.

Copyright (C) 2013 Brendan Betts (brendan.betts@live.com)

License: GNU LGPL

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

Created on Jun 25, 2013
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