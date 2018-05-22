import sys, time
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLCDNumber, QSpinBox, QVBoxLayout, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal

class Window(QWidget):
    '''Developing the GUI'''
    def __init__(self):
        '''Initialization of the GUI'''
        super(Window, self).__init__()
        
        self.set_speed = QLCDNumber(self)
        self.button = QPushButton('Start', self)
        self.progress = QProgressBar(self)
        self.button.clicked.connect(self.initUI)
        self.close=QPushButton('Close', self)
        self.close.clicked.connect(self.closeEvent)        
        layout = QVBoxLayout(self)
        layout.addWidget(self.spinbox)
        layout.addWidget(self.close)
        layout.addWidget(self.lcdnumber)
        layout.addWidget(self.button)
        layout.addWidget(self.progress)
        self.setWindowTitle('Gauges')
        
        
'''deterimining the deisred state'''
import Speedometer as sp

class cruise_control():
    desired_speed=0
    set_speed=None
    def __init__(self):
        super().__init__()
        self.set_speed()        
    def resume(self):
        '''Resume the vehicle to the previously set speed'''
        
    def set_speed(self):
        '''Set the current read speed as the desired speed'''
        a=sp.speedometer.find_speed(self)
        print(a)
    
    def run(self):
        '''Maintain the deisred speed via a PID class'''
        
        
    def on_off(self):
        '''Determine whether the crusie module is active'''
        
    def cancel(self):
        '''Cancels cruise, but still maintains the knowns speed'''
        
        
if __name__=="__main__":
    ex=cruise_control()
	app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    
        