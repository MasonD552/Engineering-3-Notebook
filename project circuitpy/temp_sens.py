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


