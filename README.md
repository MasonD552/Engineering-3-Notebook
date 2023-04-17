# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).


## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [CircuitPython_Distance_Sensor](#CircuitPython_Distance_Sensor)
* [CircuitPython_TemperatureSensor](#CircuitPython_TemperatureSensor)
* [CircuitPython_RotaryEncoder](#CircuitPython_RotaryEncoder)
* [CircuitPython_Photointerrupter](#CircuitPython_Photointerrupter)
* [Baseball_Throwing_Robot](#Baseball_Throwing_Robot)
* [PingPongBall_Levitation](#PingPongBall_Levitation)

---

## Hello_CircuitPython

### Description & Code
Hello circuit py was the first thing we were tasked to do. It is telling the board to blink its neopixel(led) and to print on the serial monitor "make it red!".

Here's how you make code look like code:

```python
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    dot.fill((0, 0, 255))
```


### Photos and Evidence

![145814267_Adafruit_METROM0Express](https://user-images.githubusercontent.com/91158978/198708119-35b39fbd-a743-4cc4-a80d-7e63b9182b00.jpg)

Image credit goes to [METRO M0 Express - Adafruit | Mouser](https://www.mouser.com/new/adafruit/adafruit-metro-mo/)


### Reflection
So the one thing that was challenging was setting up VS code so it would be able to run circuit python, and the library for the neopixel had to updated. So I had to look at the instruction on canvas and follow them in order to fix my problem. I learned that in order to update a library you need to get the up to date version and drop the specific file you need to update.
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code
The Servo is moving between a suplementary angle and movie 1 degree at a time. It is moving the angle every 0.05 seconds.

```python
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin D2.
pwm = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 1):  # 0 - 180 degrees, 1 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -1): # 180 - 0 degrees, 1 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
#lol

```

### Evidence

![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/91158978/193044181-e92b6f3c-3434-4e6b-a242-86af502cbd56.gif)

### Wiring
![Exquisite Gogo-Blad](https://user-images.githubusercontent.com/91158978/193046598-dc07286b-8199-4008-a6be-15ca5dddda87.png)

### Reflection
The one thing that was hard was understanding how a servo works. By definition "A Servo Motor is a small device that has an output shaft. This shaft can be positioned to specific angular positions by sending the servo a coded signal. As long as the coded signal exists on the input line, the servo will maintain the angular position of the shaft." So to simplify they have a library that makes it way easier to control a servo motor. I learned this by using Kattni Rembor for Adafruit Industries's code. In his website explains how the code works. https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuitpython-servo


## CircuitPython_Distance_Sensor

### Description & Code
Neopixel color changes color based on input from distance sensor.

```python
#Mason Divers
#Distance sensor that changes the color of the Neopixel based on distance.
#Thanks Grant for part of the code.
import time
import board
import adafruit_hcsr04
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
Grant = neopixel.NeoPixel(board.NEOPIXEL, 1)#connecting the neopixel on the board to the code
Grant.brightness = .3  #setting the brightness of the light, from 0-1 brightness

while True:
    try:
        cm = sonar.distance
        print((sonar.distance))
        time.sleep(0.5)
        if cm < 5:
            Grant.fill((255, 0, 0))#setting the color with RGB values
        if cm > 5 and cm < 20:
            Grant.fill((255, 255, 0))#setting the color with RGB values
        if cm > 20:
            Grant.fill((0, 255, 0))#setting the color with RGB values
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

```
```python
#Mason Divers
#Different version from the distance sensor. This distance sensor fades from red to green to blue.
#thanks graham gilb for part the code
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
Grant = neopixel.NeoPixel(board.NEOPIXEL, 1)#connecting the neopixel on the board to the code
Grant.brightness = .3  #setting the brightness of the light, from 0-1 brightness

while True:
    try:
        cm = sonar.distance
        simpleio.map_range(cm, 0, 20, 3, 20)
        print((sonar.distance))
        if cm < 7.5:
            red = simpleio.map_range(cm, 0, 6.5, 255, 0)
            green = simpleio.map_range(cm, 5, 7.5, 0, 230)
            Grant.fill((red, green, 0))
        if cm > 7.5 and cm < 12.5:
            green = simpleio.map_range(cm, 7.5, 10, 255, 0)
            blue = simpleio.map_range(cm, 9, 12.5, 0, 230)
            Grant.fill((0, green, blue))
        if cm > 12.5 and cm < 17.5:
            blue = simpleio.map_range(cm, 12.5, 15, 255, 0)
            red = simpleio.map_range(cm, 14, 17.5, 0, 240)
            Grant.fill((red, 0, blue))
        time.sleep(0.01)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
```

### Evidence

#### Pictures:
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/91158978/192557053-d899b15d-2e22-4626-91d8-de9a6d08f2f3.gif)

### Wiring
![Exquisite Gogo-Blad (1)](https://user-images.githubusercontent.com/91158978/193048333-84f23653-4f30-46e1-9c1e-7a27a48d0d50.png)

### Reflection
The one thing that was hard was getting the colors to fade in and out. I solved this by thinking to myself how I needed to use the greater than and less than. I also asked grant how he used the greater than and less than. He told me that you have to make red a certain distance the same for green and blue.



## CircuitPython_LCD

### Description & Code

```python
#Mason Divers
#LCD counter counts up when one button is held and the other buttton is pressed.
#Thank you Kaz Shinozaki for your beautiful code.
import board
import math
import time
from lcd.lcd import LCD                                     #[4-14] code to connect 
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface   #input pins to board
from digitalio import DigitalInOut, Direction, Pull
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
btn = DigitalInOut(board.D3)
btn2 = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn2.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.pull = Pull.UP
num = 0                         #Display Variable
Redo = True                     #[16-17] Variable to "debounce" button

lcd.print("Starting")
while True:                                 #[19-30] Code to add and subtract 
    if btn.value == True and Redo == True:  #from variable and 
        if btn2.value == True:              #"debounce" the  #buttons.         
            num = num + 1
        else:
            num = num - 1                                   
        lcd.clear()
        lcd.print(str(num))
        Redo = False
        time.sleep(.1)
    elif btn.value == False and Redo == False:
        Redo = True

```

### Evidence
![ezgif com-gif-maker](https://user-images.githubusercontent.com/91158978/198723378-2b73a4d7-467a-48c3-b714-d60a909e4de3.gif)


### Reflection
Hardest part was trying to get the button to work. When I have used pullup buttons they always seem to work weird. For my solution I needed to have the button be pressed down to count down and press one button to count up.


## CircuitPython_MotorControl

### Description & Code

```python
#Mason Divers
#Controlled dc motor with potentiometer. Create a circuit and code to map a potentiometer.
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
```

### Evidence
![maxresdefault](https://user-images.githubusercontent.com/91158978/200862809-39ce8413-5778-46be-bf50-6e093b70533c.jpg)
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/91158978/200862857-73220d4c-14a8-48b9-96c0-2a28158ca28d.gif)
![image](https://user-images.githubusercontent.com/91158978/200863879-123176e0-665f-483e-b1fd-2a36f44eb593.png)

Image credits go to [Santosh Das](https://www.electronicsandyou.com/blog/how-to-convert-ac-to-dc-using-diode.html) and wiring creds go to [Kazuo Shinozaki](https://github.com/kshinoz98/CircuitPython) and [Lucia Whitmore](https://github.com/lwhitmo?tab=repositories)



### Reflection
Hardest part of the assignment was making the wiring work. In order to make an effective circuit you need to have an effective batter pack that gives out the correct voltage. I solved this by using a multimeter to measure how much output was being emmited.


## CircuitPython_TemperatureSensor

### Description & Code

```python

import time
import board
import analogio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# Initialize the TMP36 sensor and the I2C LCD screen
tmp36 = analogio.AnalogIn(board.A0)
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)


def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10

# Define the desired temperature range
min_temp = 70
max_temp = 75

while True:
    # Read the temperature from the TMP36 sensor
    temp_c = tmp36_temperature_C(tmp36)
    temp_f = (temp_c * 9 / 5) + 32

    # Print the temperature
    lcd.print("Temp: {:.1f} F".format(temp_f))
    time.sleep(1)
    lcd.clear()
    
    

    # Print a message on line 2 of the LCD screen depending on the temperature
    if temp_f >= min_temp and temp_f <= max_temp:
        lcd.print("It feels good :)")
    elif temp_f < min_temp:
        lcd.print("brrr Too Cold!")
    elif temp_f <= 69.9 and temp_f >= 69.0:
        lcd.print ("Damn its sexy")
    else:
        lcd.print("Too Hot!")

```

### Evidence


![temperature sensor](https://user-images.githubusercontent.com/91158978/225392515-f7963519-f121-4666-8363-15c800b6bdc8.gif)

| TMP36 Sensor 	| CircuitPython Board 	| I2C LCD Backpack 	|
|--------------	|---------------------	|------------------	|
| VCC          	| 5V                  	| N/A              	|
| GND          	| GND                 	| GND              	|
| OUT          	| A0                  	| N/A              	|

| I2C LCD Backpack 	| CircuitPython Board 	|
|------------------	|---------------------	|
| GND              	| GND                 	|
| VCC              	| 5V                  	|
| SDA              	| SDA                 	|
| SCL              	| SCL                 	|

Note that the specific pins used for the I2C LCD backpack may vary depending on the board you're using. Be sure to check the pinout diagram for your board to ensure you're using the correct pins. Also, be sure to double-check the pinout diagrams for your components to ensure you're connecting everything correctly.

[![](https://mermaid.ink/img/pako:eNptkk1PwzAMhv-KyQmk7QBIHHpAYi1fEpMm2G3l4C3OGikfk-OCpm3_nbQdB9h6ap33eexU3qlV1KQKZVz8XjXIAvOqDpCfh907oQZpCIT8hhilZQLD0ffF-XR2eweJQop8gPH4fl_G8EXZcBYpySXbJpAIT9gwhYas7GFyWTpC7pm3soK0YqJwNYww6bRQLmDGNpx6YwBnA8E1RPNP8DkIyl5QLSoSYt9lu5inlHBN3SibXvwruoElJtLd979exVFY9cLHxas5mcYm-LbS2IHVlCxnFWNYUzFc4Oh47B1PC4OFwXHy1hG8ChjKfwjWTCiQJQ0x_QGej0C2s4--u9E4t5ctLJkZ5jFCGZ2--AO9nIFM61wff4kypNVI-XyOVudN2HWVWmXCU62K_KrJYOukVnU45Ci2Ej-2YaUK4ZZGqt1oFKosrhm9yt1cylXSViJPh-3ql-zwA-mwzyw?type=png)](https://mermaid.live/edit#pako:eNptkk1PwzAMhv-KyQmk7QBIHHpAYi1fEpMm2G3l4C3OGikfk-OCpm3_nbQdB9h6ap33eexU3qlV1KQKZVz8XjXIAvOqDpCfh907oQZpCIT8hhilZQLD0ffF-XR2eweJQop8gPH4fl_G8EXZcBYpySXbJpAIT9gwhYas7GFyWTpC7pm3soK0YqJwNYww6bRQLmDGNpx6YwBnA8E1RPNP8DkIyl5QLSoSYt9lu5inlHBN3SibXvwruoElJtLd979exVFY9cLHxas5mcYm-LbS2IHVlCxnFWNYUzFc4Oh47B1PC4OFwXHy1hG8ChjKfwjWTCiQJQ0x_QGej0C2s4--u9E4t5ctLJkZ5jFCGZ2--AO9nIFM61wff4kypNVI-XyOVudN2HWVWmXCU62K_KrJYOukVnU45Ci2Ej-2YaUK4ZZGqt1oFKosrhm9yt1cylXSViJPh-3ql-zwA-mwzyw)


### Reflection
Hardest part of the assignment was making the wiring work. In order to make an effective circuit you need to have an effective batter pack that gives out the correct voltage. I solved this by using the person next tot me to ask how they figured it out. S/O to Cooper.



## CircuitPython_RotaryEncoder

### Description & Code
The rotary encoder is connected to two digital pins of the board and generates pulses that are used to determine the direction and amount of rotation. The code uses the rotaryio library to read the encoder position and the board library to initialize the hardware.

The code also uses the digitalio library to read a push button that is connected to another digital pin of the board. When the button is pressed, the code changes the color of a single neopixel LED, based on the current position of the rotary encoder.
The code also uses the neopixel library to initialize the neopixel LED and set its brightness. Finally, the code uses the lcd.lcd library and the i2c_pcf8574_interface library to initialize an LCD display with two rows and sixteen columns. The LCD display is used to print the current color based on the position of the rotary encoder.

```python
#Mason Divers Rotary Encoder
#Thanks to River Lewis for the code and wiring diagram
#rivques
import rotaryio
import board
import digitalio
import neopixel
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

led: neopixel.Neopixel = neopixel.NeoPixel(board.NEOPIXEL, 1) # initialization of hardware
print("neopixel")

led.brightness = 0.1

button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

colors = [("stop", (255, 0, 0)), ("caution", (128, 128, 0)), ("go", (0, 255, 0))]

encoder = rotaryio.IncrementalEncoder(board.D3, board.D4, 2)
last_position = None
while True:
    position = encoder.position
    if last_position is None or position != last_position:
        lcd.clear()
        lcd.print(colors[position % len(colors)][0])
    if(not button.value):
        led[0] = colors[position % len(colors)][1]
    last_position = position
```
### Evidence
![ezgif com-video-to-gif (1)](https://user-images.githubusercontent.com/91158978/227224618-ee92a732-fee3-4975-aa4f-ac145791eef5.gif)

| Rotary Encoder Pin | Board Pin |
| ------------- | ------------- |
| Pin 1(GND) | GND  |
| Pin 2(A) | D3  |
| Pin 3(B) | D4  |

| Push Button Pin | Board Pin |
| ------------- | ------------- |
| Pin 1 | D2 |
| Pin 2 | GND  |

| Neopixel LED Pin | Board Pin |
| ------------- | ------------- |
| VIN | 3V |
| GND | GND |
| DIN | NEOPIXEL |
| LCD | Display Pin Board Pin |
| VSS | GND |
| SDA | SDA |
| SCL | SCL |

### Reflection
The code demonstrates the use of hardware components such as rotary encoders, push buttons, neopixel LEDs, and LCD displays in a project. The code is well-structured, and the comments in the code make it easy to understand. Hardest part of this assignment was getting the code to push to Github. Big thanks to [River Lewis](https://rivques.github.io/high-school-engineering/eng-3-code-notebook/) for the code. 

## CircuitPython_Photointerrupter

### Description & Code
The given code is a Python script that utilizes the CircuitPython library to interface with a photoelectric sensor (photointerrupter) connected to the D7 pin on a microcontroller board. The script starts by importing the necessary libraries, including "time" for timekeeping, "digitalio" for digital input/output, and "board" for pin mapping.

A digital input pin (photoI) is defined using the "DigitalInOut" class from the digitalio library, and its direction is set to INPUT with a pull-up resistor enabled. A "last_photoI" variable is initialized to True, and a "last_update" variable is set to -4 to keep track of the last time the crossing count was updated.

Inside the while loop, the script checks if the time elapsed since the last update is greater than 4 seconds using "time.monotonic()". If it is, the current number of crosses detected by the photoelectric sensor (photoICrosses) is printed, and the last_update time is updated.

The script then checks if the current value of the photoI pin is different from the last recorded value, and if it is low (indicating a crossing event). If so, the photoICrosses count is incremented by 1, and the last_photoI value is updated.
```python
##Mason Divers Photointerrupter
#Thanks to River Lewis for the code and wiring diagram
#rivques
import time # Import the time module for time-related functions
import digitalio # Import the digitalio module for working with digital I/O pins
import board # Import the board module for working with board-specific pin names

# Set up a digital input pin for the photoI sensor
photoI = digitalio.DigitalInOut(board.D7)
photoI.direction = digitalio.Direction.INPUT # Set the direction of the pin as input
photoI.pull = digitalio.Pull.UP # Enable the internal pull-up resistor for the pin

last_photoI = True # Initialize the previous state of the photoI sensor as True (HIGH)
last_update = -4 # Initialize the last update time as -4 seconds ago

photoICrosses = 0 # Initialize the counter for photoI sensor crossings as 0

while True: # Start an infinite loop
    if time.monotonic() - last_update > 4: # Check if 4 seconds have passed since the last update
        print(f"The number of crosses is {photoICrosses}") # Print the number of crossings
        last_update = time.monotonic() # Update the last update time to the current time

    if last_photoI != photoI.value and not photoI.value: # Check if the state of the photoI sensor has changed from HIGH to LOW (crossing detected)
        photoICrosses += 1 # Increment the counter for photoI sensor crossings
    last_photoI = photoI.value # Update the previous state of the photoI sensor with the current state
```
### Evidence
![photointcircuit](https://user-images.githubusercontent.com/91158978/230910242-def84ab4-9095-48e5-a069-461ced04de3a.png)
![ezgif com-optimize (1)](https://user-images.githubusercontent.com/91158978/231176515-50d558a7-5bdb-47a7-b968-8edae073cb41.gif)


### Reflection
Overall, the code is to be a basic implementation for detecting crossings using a photoI sensor and keeping track of the number of crossings that occur over time. However, it may need additional error handling, input validation, and other features depending on the specific application or use case.


## Baseball_Throwing_Robot
### What is this Project? 
Build a robot arm that can do a task.

### Requirements For Project 
-Your robot arm can pick something up or hold something, and move it around.  This is very general, and should be made more specific, based on the particular problem that you're attempting to solve.

-Your robot arm's motion should have 3-6 servos Micro or standard. 

-This robot arm is controlled with Arduino or CircuitPython, your choice.  The controller should run off either power coming from USB or a rechargeable 9V battery or battery pack.

-Like all of your prior projects, there should be an easy way to switch off the power, an easy way to change batteries, and some obvious indication when power is on.

-Knock out your design in CAD before you start constructing anything.  Use SolidWorks to do a motion and/or stress analysis of your robot arm or some part of the arm. 

### Project planning doccument:
Source for Project Planning:
https://docs.google.com/document/d/15Tew-MtXxxcetKLdX3Wt4Nufw6axhEezAe_4fcUIpyI/edit#heading=h.ukbi0a75zb46 

### Our goal/ Vision:
What we wanted to do as a team is create a solution to our problem. Our problem being how can we get extra practice when we dont have other people who want to come out and get extra practice. Our solition: create a robot arm that can be used as a multi-purpouse tool and can be there when the person is not.This is why we chose to make a robot arm that can throw baseballs and give you infeild repetitions when you need. Making this will eliminate the need for another person to be there and will help give you the perfect reps every time.

### Onshape documents 
![image](https://user-images.githubusercontent.com/113116205/228252030-547f0788-dd24-46d4-897a-e9394a541afd.png)
This is what we based our whole project off of it is called a jai alai scooper it holds the ball and throwis it at almost 90 degree angle and can whip the ball out of the jai alai pretty fast and was very essential in our project.

- this is a video of what the jai ali is actually capable of: https://www.youtube.com/watch?v=wk4-fuGAwjY
- here is another video:


https://user-images.githubusercontent.com/91158978/228271775-c3338992-b1db-4201-a7a4-3339b8b70e48.mp4
- here is another video of robot engineers in Philly who created a robot that through the first pitch

https://user-images.githubusercontent.com/91158978/228272692-2c9db49b-105a-4e4e-b5eb-860517c765e6.mp4







![image](https://user-images.githubusercontent.com/113116205/228253333-abcd3984-5490-450f-a9f3-8cc0a87c59f8.png)
![image](https://user-images.githubusercontent.com/113116205/228253504-3adfd3d6-4590-47cb-87a2-462effc2bb48.png)

- This is what we called our connector peice its used to conect the jai alai to the actual metal peice so we can throw the ball. How it works is we put the jai alai threw the open hole (friction fitted) and then screw in a peice that is connected to the botton to an L shaped base peice.

![image](https://user-images.githubusercontent.com/113116205/228255034-a1f2eb2d-ef10-4b09-9f2b-514ce2137940.png)

- This is on of the variations we used to build our desighns we knew we were going to lift it into the air and they had to be strapped to a platform so we used these( called l shape screw holders) to change the level because we lifted it of of the ground and then pushed them against the elevated surface and screwed them to the platform so it is stable.

![image](https://user-images.githubusercontent.com/113116205/228258049-55a11193-5c70-4fb2-8930-6919004440f8.png)
![image](https://user-images.githubusercontent.com/113116205/228258162-3137ef31-c18f-4a48-8ee1-6aedd0001f3f.png)
![image](https://user-images.githubusercontent.com/113116205/228258294-2da5d978-8b1b-469a-9ef8-278d7af61137.png)
![image](https://user-images.githubusercontent.com/113116205/228258455-16e856e2-5c4f-42de-82e5-58dae5b6e186.png)
![image](https://user-images.githubusercontent.com/113116205/228258660-affc144c-b90f-4056-8be8-3a65e897cd77.png)
![image](https://user-images.githubusercontent.com/113116205/228258746-dd44368d-8829-4be7-8636-70b526c16bc0.png)

- These are pictures of our final onshape doccument assembly with the walls and the arm being able to be able to turn 360 degrees.We change stuff to use less material in our actuall one but this is the final onshape doccument. 

### Onshape Doccument 
- https://cvilleschools.onshape.com/documents/356c56ca499f7db8076fcbc8/w/f6d4ab2399876fcf0f8c09f6/e/9266c3aeabd5a4af2e413943

### Photos Of Final Project
![IMG-2209](https://user-images.githubusercontent.com/91158978/228259502-d665096a-e785-485d-af83-426343239fdc.jpg)
![image_50445057](https://user-images.githubusercontent.com/91158978/228259522-ee10264c-3d3c-477f-a468-ec29ad1d4b8e.JPG)
![image_50403329](https://user-images.githubusercontent.com/91158978/228259537-6af1d40e-7f32-4f0e-8347-183dfa58d45a.JPG)

### Commented Code
```python
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
```
# Videos from Project

https://user-images.githubusercontent.com/91158978/228269459-0703f06c-6a79-47bb-87a3-f3d1d6f57633.mp4


https://user-images.githubusercontent.com/91158978/228269484-28800e23-5790-4bf4-9498-d971a8ff5251.mp4



https://user-images.githubusercontent.com/91158978/228269600-a4db18a1-2ca0-43e0-84d3-42527a54ff74.MOV



https://user-images.githubusercontent.com/91158978/228269615-9e9cc8d4-0779-400c-96f6-061e618b7958.MOV



### Reflection
This project taught us a lot about robotics and problem-solving. We had to come up with a solution for the problem of not having enough people to practice with, and we decided to create a robot arm that could throw baseballs and give infield repetitions. We learned how to design and build a robot arm that could move and pick up objects with the help of servos and an Arduino controller. The CAD design was especially useful in creating a motion and stress analysis of the robot arm.

One of the most challenging parts of the project was getting the arm to move in the right way to throw the baseballs accurately. We had to experiment with different designs and angles to get the throwing motion just right. We also had to figure out how to make the arm stable and secure, so it wouldn't wobble or move while throwing the ball. Another challenge was making sure the controller was working correctly and that we could easily switch off the power or change batteries.

Our main goal was to create a multi-purpose tool that could help people get extra practice without needing another person there. We wanted to eliminate the need for someone to throw the ball and give people the perfect reps every time. The jai alai scooper was a crucial component of our design, and we based the whole project on it. The connector piece was also essential in connecting the jai alai to the actual metal piece and throwing the ball accurately.

Overall, this project was a great learning experience, and we were able to develop new skills in robotics and problem-solving. It was a challenging but rewarding project, and we're proud of the final result.

## PingPongBall_Levitation

### What is this Project?

### Requirements For Project

### Project planning doccument:

### Our goal/ Vision:

### Onshape documents 

### Photos Of Final Project

### Commented Code

### Videos from Project

### Reflection
