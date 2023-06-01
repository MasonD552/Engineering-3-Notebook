import board
import adafruit_hcsr04
from PID_CPY import PID  
import pwmio   
import time 

pid = PID(100,800,1000)
pid.setpoint = 35
pid.output_limits = (24000,34000)

fanMotor = pwmio.PWMOut(board.D8,duty_cycle = 65535,frequency=5000) # fanfanMotor
fanMotor.duty_cycle = 0

dist = adafruit_hcsr04.HCSR04(trigger_pin = board.D3, echo_pin = board.D2)

while True:
    try:
        height = 20 - dist.distance
        speed = int(pid(height))
        fanMotor.duty_cycle = speed
        print("speed")
        print(speed)
        print("height")
        print(height)
        print(" ")
    except RuntimeError:
        print("retry")
    time.sleep(.1)
