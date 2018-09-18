from PyQt5.QtCore import *

class SmartBool(QObject):

    valueChanged = pyqtSignal(bool)         # Signal to be emitted when value changes.

    def __init__(self):
        super(SmartBool, self).__init__()   # Call QObject contructor.
        self.__value = False                # False initialized by default.

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self.__value != value:
            self.valueChanged.emit(value)   # If value change emit signal.
            self.__value = value