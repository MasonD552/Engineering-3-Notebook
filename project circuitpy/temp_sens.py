import time
import board
import analogio
import adafruit_character_lcd.character_lcd_i2c as character_lcd
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# Initialize the TMP36 sensor and the I2C LCD screen
tmp36 = analogio.TMP36(board.A0)
lcd_columns = 16
lcd_rows = 2
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

# Define the desired temperature range
min_temp = 20
max_temp = 25

while True:
    # Read the temperature from the TMP36 sensor
    temp_c = tmp36.temperature
    temp_f = (temp_c * 9 / 5) + 32

    # Print the temperature on line 1 of the LCD screen
    lcd.clear()
    lcd.message = "Temp: {:.1f} F".format(temp_f)

    # Print a message on line 2 of the LCD screen depending on the temperature
    if temp_c >= min_temp and temp_c <= max_temp:
        lcd.message += "\nIt feels great in here"
    elif temp_c < min_temp:
        lcd.message += "\nbrrr Too Cold!"
    else:
        lcd.message += "\nToo Hot!"

    # Wait for 1 second before updating the temperature and message again
    time.sleep(1.0)
