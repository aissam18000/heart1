from microbit import *
from maqueen import Maqueen

# Initialize Maqueen robot
mq = Maqueen()

# Main loop
while True:
    # Read accelerometer values
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    
    # Adjust motor speeds based on accelerometer readings
    left_speed = 0
    right_speed = 0
    
    # Adjust speeds based on accelerometer readings
    if y < -300:
        # Move forward
        left_speed = 100
        right_speed = 100
    elif y > 300:
        # Move backward
        left_speed = -100
        right_speed = -100
    elif x < -300:
        # Turn left
        left_speed = -50
        right_speed = 50
    elif x > 300:
        # Turn right
        left_speed = 50
        right_speed = -50
    
    # Set motor speeds
    mq.setMotor(left_speed, right_speed)
    
    # Delay to avoid excessive loop speed
    sleep(100)
