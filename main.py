#!
# import the time module
from machine import Pin
import time
import json
import math
import utime
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

push_button = Pin(13, Pin.IN)

# Opening JSON file
config_file = open('configs.json')
# Load configs
configs = json.load(config_file)

# LCD CONFIGS
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    

# Heart
heart = bytearray([0x00,0x00,0x1B,0x1F,0x1F,0x0E,0x04,0x00])

# Add custom char
lcd.custom_char(0, heart)

# Clear Lcd
lcd.clear()

def red_lights(status):
    led = Pin(14, Pin.OUT)
    if status == 1:
        led.value(1) 
        return
    else:
        led.value(0) 


def green_lights(status):
    led = Pin(15, Pin.OUT)
    if status == 1:
        led.value(1) 
        return
    else:
        led.value(0)

while True:
    red_lights(0)
    green_lights(1)
    if push_button.value():
        lcd.clear()
        # t = 25*60
        t = configs['timer']
        blink = configs['blink']
        start_message = configs['start_message']
        end_message = configs['end_message']
        lcd.putstr(start_message + chr(0))    
        if t:
            # Turn On RED LIGHTS
            green_lights(0)
            red_lights(1)

        while t:
            if t < blink:
                red_lights(t % 2)
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            lcd.move_to(5,1)
            lcd.putstr(timer)
            time.sleep(1)
            t -= 1

        # Turn On GREEN LIGHTS
        red_lights(0)
        green_lights(1)
        lcd.clear()
        lcd.putstr(end_message)
