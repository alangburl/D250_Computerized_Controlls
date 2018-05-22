import Speedometer as sp

'''Defining set-up parameters'''
cruise=None

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
    
        