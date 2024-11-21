from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

pan =  90
tilt = 90

kit.servo[0].angle=pan
kit.servo[1].angle=tilt

def move_right():
    global pan
    if pan == 0:
        pan =180
        pan -= 5 
    else:
        pan -= 5
    kit.servo[0].angle=pan
    kit.servo[1].angle=tilt


def move_left():
    global pan
    if pan == 180:
        pan =0
        pan += 5 
    else:
        pan += 5
    kit.servo[0].angle=pan
    kit.servo[1].angle=tilt

def move_up():
    global tilt
    tilt -= 5
    kit.servo[0].angle=pan
    kit.servo[1].angle=tilt

def move_down():
    global tilt
    tilt += 5
    kit.servo[0].angle=pan
    kit.servo[1].angle=tilt

def move_init():
    print(1)
