import numpy as np
from time import sleep

def forward(Rover):
    Rover.brake = 0
    if Rover.vel < Rover.max_vel:
        Rover.throttle = Rover.throttle_set #accelerate
    else:
        Rover.throttle = 0
    Rover.mode = 'forward'
    
    

def steer(Rover):
    avg_nav_angle = np.mean(Rover.nav_angles* 180/np.pi)    #can be +-45°
    Rover.steer = np.clip(avg_nav_angle-(Rover.steer/3), -15, 15) 

def stop(Rover):
    Rover.throttle = 0
    Rover.brake = Rover.brake_set
    Rover.steer = 0
    Rover.mode = 'stop'

def turn(Rover):
    Rover.throttle = 0
    Rover.brake = 0
    Rover.steer = -15
    

def CheckStucked(Rover):   
    sleep(0.5)
    if Rover.vel<=0.05:
        Rover.brake = 0
        Rover.steer = -5



def decision_step(Rover):
    # Check if we have vision data to make decisions with
    if Rover.nav_angles is not None:
        
        if Rover.vel >= 0.1:    #forward moving maybe increase to 0.2
           
            if len(Rover.nav_angles) >= Rover.stop_forward:
                forward(Rover)
                steer(Rover)  
            else:
                stop(Rover)

        else:
            if len(Rover.nav_angles) >= Rover.go_forward:
                forward(Rover)
                steer(Rover)
                #CheckStucked(Rover)
            else:
                turn(Rover)  
                
    # Just to make the rover do something 
    # even if no modifications have been made to the code
    else:
        Rover.throttle = Rover.throttle_set
        Rover.steer = 0
        Rover.brake = 0

    return Rover

