import sys, time
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, 
                             QLCDNumber, QVBoxLayout, QProgressBar,QCheckBox,
                             QRadioButton,QHBoxLayout)
from PyQt5.QtCore import QThread, pyqtSignal


class Display(QWidget):
    def __init__(self):
        super().__init__()
        
        self.throttle_position=QProgressBar(self)
        self.speed=QLCDNumber(self)
        self.set_speed=QLCDNumber(self)
        self.cruise_indicator=QRadioButton(self)
        
        self.cruise_widget=QWidget(self)
        
        self.cruise_layout=QHBoxLayout(self)
        self.cruise_layout.addWidget(self.cruise_indicator)
        self.cruise_layout.addWidget(self.set_speed)
        self.cruise_widget.layout=self.cruise_layout
        
        self.layout=QVBoxLayout(self)
        self.layout.addWidget(self.throttle_position)
        self.layout.addWidget(self.speed)
        self.layout.addWidget(self.cruise_widget)
        
    
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Display()
    window.show()
    sys.exit(app.exec_())