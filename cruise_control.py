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
#        self.button.clicked.connect(self.initUI)
        self.close=QPushButton('Close', self)
#        self.close.clicked.connect(self.closeEvent) 
        self.cruise=cruise_control()
        layout = QVBoxLayout(self)
        layout.addWidget(self.close)
        layout.addWidget(self.set_speed)
        layout.addWidget(self.button)
        layout.addWidget(self.progress)
        self.setWindowTitle('Gauges')
        self.set_speed.display(self.cruise.set_speed())
        
        
'''deterimining the deisred state'''
import Speedometer as sp
from PID import calculate

class cruise_control():
    desired_speed=0
    def __init__(self):
        super().__init__()
        self.on_off()        
    def resume(self):
        '''Resume the vehicle to the previously set speed'''
        
    def set_speed(self):
        '''Set the current read speed as the desired speed'''
        self.desired_speed=sp.speedometer.find_speed(self)
        return self.desired_speed
    
    def run(self):
        '''Maintain the deisred speed via a PID class'''
        self.actual_speed=sp.speedometer.find_speed(self)
        while self.on_off==True:
            scalar=calculate(self.set_speed(),self.actual_speed,.001,20,20,20)
            
        
    def on_off(self):
        '''Determine whether the crusie module is active'''
        on_off=True
        return on_off
        
    def cancel(self):
        '''Cancels cruise, but still maintains the knowns speed'''
            
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    
        