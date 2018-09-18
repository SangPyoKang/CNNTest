from PyQt5.QtWidgets import QDialog,QWidget,QPushButton
from BasicFunction.SmartBoolean import SmartBool



class QImageDialog(QDialog) :

    def initBoard(self, parent=None):
        '''Init Board'''
        # self.checkable = True
        self.pressed(True)
        # self.clicked(False)
        # self.setGeometry(300,300,250,150)
        # self.show()
