import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    dot.fill((0, 0, 255))