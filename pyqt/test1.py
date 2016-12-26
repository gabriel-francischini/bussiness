#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from janela_principal import Ui_JanelaPrincipal


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QMainWindow()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    y = Ui_JanelaPrincipal()
    y.setupUi(w)

    w.show()
    
    sys.exit(app.exec_())