# phil welsby - 5 feb 2021
# main function to switch ligh on/off
# works with 2 function files - function_light_on.py and function_light_off.py

from os import system
from adjustable_light_on import light_on
from adjustable_light_off import light_off

def toggle():
    system('clear')
    print('''
    (1) Adjustable Light On
    (2) Adjustable Light Off''')

    switch = input('\nEnter 1 or 2: ')
    if switch in ['1', '2']:
        if switch == '1':
            light_on()
            toggle()
        elif switch == '2':
            light_off()
            toggle()
    else:
        toggle()

toggle()
