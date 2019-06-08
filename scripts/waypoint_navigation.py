#!/usr/bin/env python

import math
import numpy as np
from crazyflieParser import CrazyflieParser

if __name__ == '__main__':

    index = 2   # for cf2
    initialPosition = [0,0,0] # x,y,z coordinate for this crazyflie
    cfs = CrazyflieParser(index, initialPosition)
    cf = cfs.crazyflies[0]
    time = cfs.timeHelper

    cf.setParam("commander/enHighLevel", 1)
    cf.setParam("stabilizer/estimator", 2) # Use EKF
    cf.setParam("stabilizer/controller", 2) # Use mellinger controller
    #cf.setParam("ring/effect", 7)

    cf.takeoff(targetHeight = 0.5, duration = 3.0)
    time.sleep(3.0)

    
    # Phase1
    cf.goTo([0.5,0,0],0,5.0,relative = True)
    time.sleep(5.0)
    cf.goTo([0,0.5,0],0,5.0,relative = True)
    time.sleep(5.0)
    cf.goTo([-0.5,0,0],0,5.0,relative = True)
    time.sleep(5.0)
    cf.goTo([0,-0.5,0],0,5.0,relative = True)
    time.sleep(5.0)
    
    '''
    # Phase2
    cf.goTo([0.5,0,0],0,4.0, relative = True)
    time.sleep(4.0)
    # circle
    for i in range(80):
        cf.cmdPosition([0.5*math.cos(i*np.pi/40),0.5*math.sin(i*np.pi/40),0.5],0)
        time.sleep(0.1)
    # Go back to origin  
    for i in range(40):
        cf.cmdPosition([0.5-0.0125*i,0,0.5],0)
        time.sleep(0.1)

    '''   
    '''
    # Phase 3
    for i in range(80):
        cf.cmdPosition([0.5*math.sin(i*np.pi/40),0.5-0.5*math.cos(i*np.pi/40),0.5],0)
        time.sleep(0.1)
    for i in range(80):
        cf.cmdPosition([0.5*math.sin(i*np.pi/40),-0.5+0.5*math.cos(i*np.pi/40),0.5],0)
        time.sleep(0.1)
    '''
    '''
    # Bonus
    # Please comment previous command for takeing off before run that part
    cf.takeoff(targetHeight = 1.0, duration = 6.0)
    time.sleep(6.0)    
    for i in range(40):
        cf.cmdPosition([0.5*math.sin(i*np.pi/40),0.5-0.5*math.cos(i*np.pi/40),1.0+i*0.5/40],0)
        time.sleep(0.1)
    for i in range(40):
        cf.cmdPosition([0.5*math.sin((i+40)*np.pi/40),0.5-0.5*math.cos((i+40)*np.pi/40),1.5-i*0.5/40],0)
        time.sleep(0.1)        
    for i in range(40):
        cf.cmdPosition([0.5*math.sin(i*np.pi/40),-0.5+0.5*math.cos(i*np.pi/40),1.0-i*0.5/40],0)
        time.sleep(0.1) 
    for i in range(40):
        cf.cmdPosition([0.5*math.sin((i+40)*np.pi/40),-0.5+0.5*math.cos((i+40)*np.pi/40),0.5+i*0.5/40],0)
        time.sleep(0.1) 
    '''
    
    # You can adjust landing time w.r.t different heights.
    cf.land(targetHeight = 0.0, duration = 5.0)
    time.sleep(5.0)
