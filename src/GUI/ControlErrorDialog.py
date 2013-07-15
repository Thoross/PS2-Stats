'''
PS2-Stats : Python module for PlanetSide 2 Stat tracking.

Copyright (C) 2013 Brendan Betts (brendan.betts@live.com)

License: GNU LGPL

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

Created on Jul 14, 2013
'''

from PySide.QtGui import *
from src.GUI.ErrorDialog import Ui_Dialog
import sys


class ControlErrorDialog(QDialog):

    def __init__(self, parent=None, *args):
        super(ControlErrorDialog,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        if args is not None:
            for arg in args:
                if arg == "No Player":
                    self.ui.lbl_error.setText("Player not found. Try again.")
        self.exec_()