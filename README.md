# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).

**Link to:https://github.com/MasonD552/Engineering-3-Notebook/tree/CAD **
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [CircuitPython_Distance_Sensor](#CircuitPython_Distance_Sensor)
* [NextAssignmentGoesHere](#NextAssignment)
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

