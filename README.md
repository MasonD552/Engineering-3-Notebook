# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
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
Description goes here

Here's how you make code look like code:

```python
Code goes here

```


### Evidence


![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone, if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code

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

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection


## CircuitPython_Distance_Sensor

### Description & Code

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

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
