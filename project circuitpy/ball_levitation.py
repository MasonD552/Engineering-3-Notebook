import board
import adafruit_hcsr04
from PID_CPY import PID  
import pwmio   
import time 

pid = PID(15000,1.0,4750)
pid.setpoint = 15.00
pid.output_limits = (20000.00,50000.00)

fanMotor = pwmio.PWMOut(board.D8,duty_cycle = 65535) # fanfanMotor
fanMotor.duty_cycle = 0

dist = adafruit_hcsr04.HCSR04(trigger_pin = board.D3, echo_pin = board.D2)

while True:
    try:
        height = 26 - dist.distance
        speed = int(pid(height))
        fanMotor.duty_cycle = speed
        print("speed ", speed, " height ", height,)
    except RuntimeError:
        print("retry")
    time.sleep(.1)
