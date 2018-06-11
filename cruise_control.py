import Speedometer as sp
from PID import calculate

class cruise_control():
    desired_speed=0
    def __init__(self):
        super().__init__()
#        self.on_off()        
    def resume(self):
        '''Resume the vehicle to the previously set speed'''
        
    def set_speed(self):
        '''Set the current read speed as the desired speed'''
        self.desired_speed=sp.speedometer.find_speed(self)
        return self.desired_speed
    
    def run(cruise_state):
        '''Maintain the deisred speed via a PID class'''
        actual_speed=sp.find_speed(self)
        past_time=time.time()
        while crusie_state==True:
            current_time=time.time()
            scalar=calculate(self.set_speed(),actual_speed,current_time-past_time,20,20,20)
            past_time=current_time
            return scalar
        
    def on_off():
        '''Determine whether the crusie module is active'''
#        number_of_hits=int
        on_off=bool
        
        
        if number_of_hits==int:
            number_of_hits=1
            on_off=True
        elif number_of_hits%2==1:
            number_of_hits+=1
            on_off=False
        elif number_of_hits%2==0:
            number_of_hits+=1
            on_off=True
        return on_off
        
    def cancel(self):
        '''Cancels cruise, but still maintains the knowns speed'''
            
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    
        