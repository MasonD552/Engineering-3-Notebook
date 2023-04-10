# Import necessary libraries
import time
from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull
from pwmio import PWMOut
from adafruit_motor import motor as Motor

# Set up DRV6612 motor driver inputs and outputs
drv6612_ain1 = PWMOut(board.D5, frequency=50)
drv6612_ain2 = PWMOut(board.D4, frequency=50)
drv6612_sleep = DigitalInOut(board.D0)

# Set up button and switch inputs
button_a = DigitalInOut(board.D13)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN
switch = DigitalInOut(board.D10)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# Set up motor using DRV6612 inputs
motor_a = Motor.DCMotor(drv6612_ain1, drv6612_ain2)
timeStop = 0.0
currentTime = time.monotonic()

# Define function to print motor status


def print_motor_status(motor):


if (motor == motor_a):
    motor_name = "A"
else:
motor_name = "Unknown"
print(f"Motor {motor_name} throttle is set to {motor.throttle}.")

# Main loop
drv6612_sleep.direction = Direction.OUTPUT
drv6612_sleep.value = True  # enable (turn on) the motor driver
while True:
    # If button and switch are both pressed
if (button_a.value == 1 & switch.value == 1):
    # Drive forward at full throttle for 5 seconds
motor_a.throttle = 1.0
timeStop = (time.monotonic() + 5)

# If switch is turned off
if (switch.value == 0):
    # Brake to a stop
    motor_a.throttle = None

# If timeStop has elapsed
if (timeStop < time.monotonic()):
    # Brake to a stop
    motor_a.throttle = None

# Print button and switch values, timeStop, current time, and motor throttle
print((button_a.value, switch.value, timeStop, time.monotonic(), motor_a.throttle))

# Use conditional variables to determine which "state" you want to be in
# If button is hit
#  tStop  = current time + 5s
#  goStop = 1
#
# If switch.val == 0
#   goStop = 0
#
# If tStop < current time
#   goStop = 0
#
# If goStop = 1
#   motor throttle = 1
# Else
#   motor throttle = 0
