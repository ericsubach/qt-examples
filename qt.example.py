#!/usr/bin/env python

import sys

from   PyQt4        import QtGui
from   PyQt4        import QtCore
from   PyQt4.QtGui  import *
from   PyQt4.QtCore import *


class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      
      self.mainLayout = QtGui.QVBoxLayout()
      
      #
      # Add widgets here.
      #
      
      #self.mainLayout.addWidget()
      
      self.centralWidget = QtGui.QWidget()
      self.centralWidget.setLayout(self.mainLayout)
      self.setCentralWidget(self.centralWidget)

      
   def run(self):
      self.show()
      

def main():
      # Window.
      tApp = QtGui.QApplication(sys.argv)
      tWindow = MainWindow()
      
      tWindow.run()
      sys.exit(tApp.exec_())

if __name__ == '__main__':
   main()
