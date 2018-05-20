import numpy as np
from sympy import *

'''Defining set-up parameters'''
cruise=None


'''Logical statements'''
def cruise_on_off(cruise):
    while switch=='On' and cruise=='On':
        switch=input("Switch Position: ")
        brake_pedal=input("Brake Pedal- Released or Depressed: ")
        set_button=input("Set Button- Released or Depressed: ")
        
        if brake_pedal=='Depressed':
            cruise='Off'
            
        else:
            cruise='On'
        
    return cruise 