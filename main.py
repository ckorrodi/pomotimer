#!
# import the time module
import time
import json

# Opening JSON file
config_file = open('configs.json')

configs = json.load(config_file)

# t = 25*60
t = configs['timer']
blink = configs['blink']
start_message = configs['start_message']
end_message = configs['end_message']

def red_lights(status):
    if status == 1:
        print("REDS - ON")
        return
    else:
        print("REDS - OFF")


def green_lights(status):
    if status == 1:
        print("GREENS - ON")
        return
    else:
        print("GREENS - OFF")


# define the countdown func.
if t:
    # Turn On RED LIGHTS
    green_lights(0)
    red_lights(1)

while t:
    if t < blink:
        red_lights(t % 2)
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(start_message + ":" + timer, end="\r")
    time.sleep(1)
    t -= 1

# Turn On GREEN LIGHTS
red_lights(0)
green_lights(1)

print(end_message, end="\r")