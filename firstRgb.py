from asyncore import loop
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.2 

print("Make it red!")

while True:
    dot.fill((255, 0, 0))
    time.sleep(0.1)
    dot.fill((0, 0, 0))
    time.sleep(0.1)
