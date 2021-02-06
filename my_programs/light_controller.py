# phil welsby - 6 feb 2021
# program to turn lamps on/off

from time import sleep
import RPi.GPIO as GPIO
from os import system

system('clear')


GPIO.setmode(GPIO.BCM)
pinList = [6, 13, 19, 26, 21, 20, 16, 12]

for i in pinList:
    GPIO.setwarnings(False)
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

def controller():
    print('''




                 (1)   Adjustable Light On
                 (2)   Adjustable Light Off
                 (3)   Lava Lamp On
                 (4)   Lava Lamp Off
                 (5)   All Lamps Off

                 (999) Exit''')

    switch = input('\nEnter choice: ')
    if switch in ['1', '2', '3', '4', '5', '999']:
        if switch == '1':
            GPIO.output(21, GPIO.LOW)
            system('clear')
            print('Adjustable Lamp On')
            sleep(1)
            controller()
        elif switch == '2':
            GPIO.output(21, GPIO.HIGH)
            system('clear')
            print('Adjustable Lamp Off')
            sleep(1)
            controller()
        elif switch == '3':
            GPIO.output(20, GPIO.LOW)
            system('clear')
            print('Lava Lamp On')
            sleep(1)
            controller()
        elif switch == '4':
            GPIO.output(20, GPIO.HIGH)
            system('clear')
            print('Lava Lamp Off')
            sleep(1)
            controller()
        elif switch == '5':
            GPIO.output(21, GPIO.HIGH)
            GPIO.output(20, GPIO.HIGH)
            system('clear')
            print('All Lamps Off')
            sleep(1)
            controller()
        elif switch == '999':
            system('clear')
            print('\nGOODBYE... All Lamps Are Off\n')
            for i in pinList:
                GPIO.setwarnings(False)
                GPIO.setup(i, GPIO.OUT)
                GPIO.output(i, GPIO.HIGH)
    else:
        print(switch, 'is not a valid option')
        print('Please try again')
        sleep(1)
        system('clear')
        controller()
controller()
