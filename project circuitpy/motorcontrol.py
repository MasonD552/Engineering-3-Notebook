#Mason Divers
#Controlled dc motor with potentiometer
#Code is credited to Grant Gastinger & Kaz Shinozaki
import board               #[lines 1-4] Importing neccesary libraries
import time
from analogio import AnalogOut, AnalogIn
import simpleio

motor = AnalogOut(board.A1) #[lines 5 & 6] Definining the motor and potentiometer
pot = AnalogIn(board.A0)

while True:
    print(simpleio.map_range(pot.value, 96, 65520, 0, 65535)) #Print mapped potentiometer value to motor inputs
    motor.value = int(simpleio.map_range(pot.value, 96, 65520, 0, 65535)) #Write the mapped value to motor
    time.sleep(.1)   