# phil welsby - 5 feb 2021
# simple program to turn off a light by switching a relay,
# on a relay board connected to a raspberry pi

#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [6, 13, 19, 26, 21, 20, 16, 12]

# loop through pins and set mode and state to 'low'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

try:
    GPIO.output(21, GPIO.HIGH)
    print ("LIGHT OFF")

# End program cleanly with keyboard
except KeyboardInterrupt:
    print ("  Quit")

# Reset GPIO settings
    GPIO.cleanup()

