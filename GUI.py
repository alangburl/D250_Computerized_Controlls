import sys, time
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, 
                             QLCDNumber, QVBoxLayout, QProgressBar,QCheckBox,
                             QRadioButton,QHBoxLayout,QGridLayout,QLineEdit)
from PyQt5.QtCore import QThread, pyqtSignal


class Display(QWidget):
    def __init__(self):
        super().__init__()
        
        self.throttle_position=QProgressBar(self)
        self.throttle_position.setMinimumHeight(50)
        self.speed=QLCDNumber(self)
        self.speed.setMinimumHeight(50)
        self.set_speed=QLCDNumber(self)
        self.set_speed.setMinimumHeight(50)
        self.cruise_indicator=QLineEdit(self)
        self.cruise_indicator.setMinimumHeight(50)
        self.set_cruise=QPushButton('Set',self)
        self.resume=QPushButton('Resume',self)
        self.cancel=QPushButton('Cancel',self)
        self.cruise_state=QPushButton('On\Off',self)
        'Add the layout to the widget'
        
        self.layout=QGridLayout(self)
        self.layout.addWidget(self.speed,0,1)
        self.layout.addWidget(self.set_speed,2,1)
        self.layout.addWidget(self.cruise_indicator,1,0)
        self.layout.addWidget(self.resume,0,2)
        self.layout.addWidget(self.set_cruise,1,2)
        self.layout.addWidget(self.cancel,3,2)
        self.layout.addWidget(self.cruise_state,4,2)
        self.setLayout(self.layout)
    
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Display()
    window.show()
    sys.exit(app.exec_())