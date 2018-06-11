import time

def find_speed():
    ''''Determine the speed from the GPIO input pins''' 
    # =============================================================================
    # define GPIO stuff here
    # =============================================================================
    frequency=22 #defined from stuff later
    
    tire_diameter=34.4 #in
    gear_ratio=3.73
    
    in_to_mile=1/(12*5280)
    
    freq_to_mph=2.2 #hz/mph
    
    speed_in_mph=frequency/freq_to_mph
    speed_in_mps=speed_in_mph/3600
    return speed_in_mph,speed_in_mps
    