import time

def find_speed():
    ''''Determine the speed from the GPIO input pins''' 
    # =============================================================================
    # define GPIO stuff here
    # =============================================================================
    start_time=time.time()
    frequency=2.2*60 #defined from stuff later

    freq_to_mph=2.2 #hz/mph

    speed_in_mph=frequency/freq_to_mph
    speed_in_mps=speed_in_mph/3600
    time.sleep(0.0001)
    
    delta_time=time.time()-start_time
    delta_mileage=speed_in_mps*delta_time
    
    return speed_in_mph,speed_in_mps,delta_mileage
    