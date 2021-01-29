# phil welsby - 27 jan 2021
# function to add items to a text file named inventory.txt
# NOTE - requires try except clause to catch errors of input by user



def get_data():
    print('\n'*100)
    name = input('Enter your name: ')
    play = input('Do you want to play? Y/n')

    inventory = open('inventory.txt', 'a')

    print('NAME:', name, '        PLAY or NOT ', play, file = inventory)
    inventory.close()


get_data()
