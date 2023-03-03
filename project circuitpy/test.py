# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time

import board
import digitalio
import time

button_a = digitalio.DigitalInOut(board.D8)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN


switch = digitalio.DigitalInOut(board.D9)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

while True:
    if button_a.value:
        print((1,))
        time.sleep(0.5)
    elif switch.value:
        print((-1,))
    else:
        print((0,))
    time.sleep(0.1)
