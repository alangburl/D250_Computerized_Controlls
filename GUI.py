import sys,time
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, 
                             QLCDNumber, QVBoxLayout, QProgressBar,
                             QGridLayout,QLineEdit,
                             QSizePolicy)
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QFont
import PyQt5.QtCore as q


class Display(QWidget):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        self.setWindowTitle('D250 Speedometer v1.0')
        font=QFont()
        font.setPointSize(16)
        
        self.throttle_position=QProgressBar(self)
        self.throttle_position.setFont(font)
        self.throttle_position.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.throttle_position.setMaximumHeight(30)
        
        self.speed=QLCDNumber(self)
        self.speed.setFont(font)
        self.speed.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        #use thread to display value
        
        self.cruise_indicator=QLineEdit(self)
        self.cruise_indicator.setReadOnly(True)
        self.cruise_indicator.setFont(font)
        self.cruise_indicator.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.cruise_indicator.setAlignment(q.Qt.AlignRight)
        self.cruise_indicator.setMaximumHeight(100)
        
        self.indicator=QLineEdit(self)
        self.indicator.setReadOnly(True)
        self.indicator.setFont(font)
        self.indicator.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.indicator.setAlignment(q.Qt.AlignRight)
        self.indicator.setMaximumHeight(100)
        
        self.set_cruise=QPushButton('Set',self)
        self.set_cruise.setCheckable(True)
        self.set_cruise.setFont(font)
        self.set_cruise.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.set_cruise.clicked.connect(self.sets)
        
        self.resume=QPushButton('Resume',self)
        self.resume.setFont(font)
        self.resume.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.resume.clicked.connect(self.resumes)
        
        self.cancel=QPushButton('Cancel',self)
        self.cancel.setFont(font)
        self.cancel.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.cancel.clicked.connect(self.cancels)
        
        self.cruise_state=QPushButton('On\Off',self)
        self.cruise_state.setCheckable(True)
        self.cruise_state.setFont(font)
        self.cruise_state.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.cruise_state.clicked.connect(self.on_off)
        
        'Add the layout to the widget'

        layout=QGridLayout()
        layout.addWidget(self.speed,0,1)
        layout.addWidget(self.cruise_indicator,1,1)
        layout.addWidget(self.indicator,2,1)
        layout.addWidget(self.resume,0,2)
        layout.addWidget(self.set_cruise,1,0,2,1)
        layout.addWidget(self.cancel,1,2,2,1)
        layout.addWidget(self.cruise_state,0,0)
        
        vlayout=QVBoxLayout()
        vlayout.addLayout(layout)
        vlayout.addWidget(self.throttle_position)
        self.setLayout(vlayout)
        self.initUI()
        
    def initUI(self):
        '''Setting up the GUI'''
        self.th=Thread(self)
        self.th.changeprogressbar.connect(self.throttle_position.setValue)
        self.th.changelcd.connect(self.speed.display)
        self.th.change_odometer.connect(self.cruise_indicator.setText)
        self.th.start()
        
    def on_off(self):
        '''State of the Cruise Control'''
        if self.cruise_state.isChecked()==True:
            self.cruise_indicator.setText('On')
        elif self.cruise_state.isChecked()==False:
            self.cruise_indicator.setText('Off')
        
    def resumes(self):
        '''Resumes the pickup to set speed'''
        self.cruise_indicator.setText('Resuming')
        time.sleep(2)
        self.th.change_odometer.connect(self.cruise_indicator.setText)
        
    def cancels(self):
        '''Cancels and keeps set speed'''
        self.cruise_indicator.setText('Cancels')
        time.sleep(2)
        self.th.change_odometer.connect(self.cruise_indicator.setText)
        
    def sets(self):
        '''Sets the speed for the cruise control'''
        self.cruise_indicator.setText('Set')
        time.sleep(2)
        self.th.change_odometer.connect(self.cruise_indicator.setText)
    
    
import Speedometer as sp
   
class Thread(QThread):
    '''Creates the thread to update the progress bar'''
    changeprogressbar=pyqtSignal(int)
    changelcd=pyqtSignal(int)
    change_odometer=pyqtSignal(str)
    
    def __init__(self, parent=None):
        '''Setting up the thread'''
        QThread.__init__(self, parent=parent)
        self.isRunning=True
    
    def run(self):
        '''Starting the thread'''
        file=open('odometer.csv','r+')
        mile=float(file.readlines()[0])
        st=time.time()
        delta=0
        while delta<6.0:
            self.changelcd.emit(int(sp.find_speed()[0]))
            delta_mileage=sp.find_speed()[2]
            mileage_new=delta_mileage+mile
            mile=mileage_new
            self.change_odometer.emit(str(round(mileage_new,2)))
#            print(mileage_new)
            speed=sp.find_speed()[0]
            if speed<0.1:
                file.seek(0,0)
                file.truncate(0)
                file.write(str(mileage_new))
                file.close()
                time.sleep(0.25)
                file=open('odometer.csv','r+')
                mile=float(file.readlines()[0])
                delta=time.time-st
            
            
    def stop(self):
        '''Stopping the thread'''
        self.isRunning=False
        #self.quit()
#        self.exit()
        
        
if __name__ == "__main__":
    start=time.time()
    app = QApplication(sys.argv)
    window = Display()
    window.show()
    sys.exit(app.exec_())
    end=time.time()