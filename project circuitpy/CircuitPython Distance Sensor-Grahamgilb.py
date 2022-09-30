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