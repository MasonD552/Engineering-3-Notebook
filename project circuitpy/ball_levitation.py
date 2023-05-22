import board
import digitalio
import pulseio
import time
import adafruit_hcsr04

# defines variables


# Geometrical parameters of the system

# variables for the control loop
controlP = 0.0
controlI = 0.0
controlD = 0.0
control = 0.0
err = 0.0
prevErr = 0.0
previousBallPos = 0.0  # the initial ball position, then updates
prevControlI = 0.0  # initial condition for integrator
prevBallPos = columnL + upperGap - ballDiam / 2  # used in control D
# array to make average of hand position
storeHandPos = [0.0, 0.0, 0.0, 0.0, 0.0]

# Initialize ultrasonic sensors
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
# Initialize PWM output
fanMotor = pulseio.PWMOut(fanPin=board.D1, frequency=1000, duty_cycle=0)
tubeLight = pulseio.PWMOut(tubeLightPin= board.D4, frequency=1000, duty_cycle=0)

# Initialize LED and Button
led = digitalio.DigitalInOut(led)
led.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(button)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
# Measure hand position
durationH = sonar.distance
distanceH = durationH / 58.2

# Measure ball position
durationB = sonarBall.distance
distanceB = durationB / 58.2

# Control loop calculations
err = ref - distanceH
controlP = 1.0 * err
controlI = prevControlI + 0.5
# PID constants
samplingTime = 0.0625  # sampling time in seconds


