# =============================================================================
# Determining position of stepper motor
# =============================================================================

import time,sys
import numpy as np
arr=[]

past_time=time.time()
for i in range(5000):
    current_time=time.time()
    delta_t=current_time-past_time
    arr.append(delta_t)
    past_time=current_time
    time.sleep(0.001)
print(np.std(arr),np.average(arr))