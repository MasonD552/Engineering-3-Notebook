#Mason Divers
#Controlled dc motor with potentiometer
#Code is credited to Grant Gastinger
import time
import board
import simpleio
from analogio import AnalogIn
import adafruit_motor

potentiometer = AnalogIn(board.A0)
motor1 = motor.DCMotor(board. D9)

print("hello world")

while True:
    print((potentiometer.value,)) 
    ticks = potentiometer.value
    spped = simpleio.map_range(ticks,0,1023,0,1)
    motor1._throttle(spped)
