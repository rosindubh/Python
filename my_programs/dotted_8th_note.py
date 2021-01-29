# program to find time in ms for echo to create a dotted 8th note delay
# phil welsby - 25 march 2020

# function to clear screen
def wiper():
    print('\n' * 100)

# clear screen
wiper()

# get user input

bpm = int(input('Enter tempo in BPM: '))

# math
quater_note = 60 / bpm * 1000
eighth_note = quater_note / 2 * 1.5

print('Set delay to', eighth_note, 'ms')
