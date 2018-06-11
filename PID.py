def calculate(desire,actual,DT, kp,kd,ki,ui_past=0,error_past=0):
    '''calculate pid controller'''                    
    uimax=10
    error= actual-desire
    up=error*kp
    ui=ki*error*DT+ui_past
    ui_past=ui
    
    if ui>uimax:
        ui=uimax
    elif ui<-uimax:
        ui=uimax
        
    ud=kd*(error-error_past)/DT
    error_past=error
    ut=up+ui+ud
    return ut
    
    
if __name__=="__main__":
    ex=calculate(2,3,4,5,6,7)