from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull
from pwmio import PWMOut
from adafruit_motor import motor as Motor

DEBUG = True  # mode of operation; False = normal, True = debug
OP_DURATION = 5  # operation duration in seconds

drv6612_ain1 = PWMOut(board.D5, frequency=50)
drv6612_ain2 = PWMOut(board.D4, frequency=50)
drv6612_sleep = DigitalInOut(board.D0)

motor_a = Motor.DCMotor(drv6612_ain1, drv6612_ain2)

def print_motor_status(motor):
    if motor == motor_a:
        motor_name = "A"
    else:
        motor_name = "Unknown"
    print(f"Motor {motor_name} throttle is set to {motor.throttle}.")

def basic_operations():
    # Drive forward at full throttle
    motor_a.throttle = 1.0
    if DEBUG: print_motor_status(motor_a)
    sleep(OP_DURATION)

    # Coast to a stop
    motor_a.throttle = None
    if DEBUG: print_motor_status(motor_a)
    sleep(OP_DURATION)

    # Drive backwards at 50% throttle
    motor_a.throttle = -0.5
    if DEBUG: print_motor_status(motor_a)
    sleep(OP_DURATION)

    # Brake to a stop
    motor_a.throttle = 0
    if DEBUG: print_motor_status(motor_a)
    sleep(OP_DURATION)

# Main
drv6612_sleep.direction = Direction.OUTPUT
drv6612_sleep.value = True  # enable (turn on) the motor driver

if DEBUG: print("Running in DEBUG mode.  Turn off for normal operation.")
while True:
    basic_operations()  # perform basic motor control operations on motor A