# phil welsby - 6 feb 2021

from time import sleep
from os import system
import RPi.GPIO as GPIO

# adjustable light on
def light_on():

    GPIO.setmode(GPIO.BCM)

    # init list with pin numbers

    pinList = [6, 13, 19, 26, 21, 20, 16, 12]

    # loop through pins and set mode and state to 'low'

    for i in pinList:
        GPIO.setwarnings(False)
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

    try:
        GPIO.output(21, GPIO.LOW)
        print ("LIGHT ON")

    # End program cleanly with keyboard
    except KeyboardInterrupt:
        print ("  Quit")

    # Reset GPIO settings

        GPIO.cleanup()


# adjustable light off
def light_off():
    GPIO.setmode(GPIO.BCM)

    # init list with pin numbers

    pinList = [6, 13, 19, 26, 21, 20, 16, 12]

    # loop through pins and set mode and state to 'low'

    for i in pinList:
        GPIO.setwarnings(False)
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

# main
def main():
    system('clear')
    print('''


                     ================================
                     === (1) Adjustable Light On  ===
                     === (2) Adjustable Light Off ===
                     === (3)    Lava Lamp On      ===
                     === (4)    Lava Lamp Off     ===
                     ================================''')

    switch = input('\n\n Choose from menu: ')
    if switch in ['1', '2']:
        if switch == '1':
            light_on()
            main()
        elif switch == '2':
            light_off()
            main()
    elif switch == '999':
        print('Goodbye...')
    else:
        system('clear')
        print('\n\n\n\n\n\n\n\n\n\n\n[ ', switch, ' ] is not a valid choice...\n') 
        sleep(2)
        print('\n Please wait and then try again try again...\n')
        sleep(3)
        main()

main()

