#Mason Divers
#Different version from the distance sensor
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