import time
from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull
from pwmio import PWMOut
from adafruit_motor import motor as Motor

drv6612_ain1 = PWMOut(board.D5, frequency=50)
drv6612_ain2 = PWMOut(board.D4, frequency=50)
drv6612_sleep = DigitalInOut(board.D0)

button_a = DigitalInOut(board.D13)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN
switch = DigitalInOut(board.D10)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

motor_a = Motor.DCMotor(drv6612_ain1, drv6612_ain2)
timeStop = 0.0
currentTime = time.monotonic()


def print_motor_status(motor):
    if motor == motor_a:
        motor_name = "A"
    else:
        motor_name = "Unknown"
    print(f"Motor {motor_name} throttle is set to {motor.throttle}.")


# Main
drv6612_sleep.direction = Direction.OUTPUT
drv6612_sleep.value = True  # enable (turn on) the motor driver

while True:

    if (button_a.value == 1 & switch.value == 1):
        #print(('Button Pressed & Switch On',))
        # Drive forward at full throttle
        motor_a.throttle = 1.0
        timeStop = (time.monotonic() + 5)
    
    if (switch.value == 0):
        #print(('Switch Off',))
        # Brake to a stop
        motor_a.throttle = None

    if (timeStop < time.monotonic()):
        #print(('timesup',))
        motor_a.throttle = None
    print((button_a.value , switch.value, timeStop, time.monotonic(), motor_a.throttle))
 
    # print(time.monotonic())

    
    # use conditional variables to determine which "state" you want to be in
    # if button is hit
    #  tStop  = current time + 5s
    #  goStop = 1
    #
    # if switch.val == 0
    #   goStop = 0
    #
    # if tStop < current time
    #   goStop = 0
    #
    # if goStop = 1
    #   motor throttle = 1
    # else
    #   motor throttle = 0
#Mason Divers