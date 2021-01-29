
# phil welsby - 12 jan 2021


# using  <from time import sleep>  imports just the sleep() bit of time
# this saves having to keep typing time.sleep(), you can just type sleep()

from time import  sleep

print('\n\nThis program will start shortly')
print('\n\nWhen this program ends:')
print('Read comments to see how time was imported into this script')
sleep(7)


# this print() command is using triple quotes  '''  '''
# allowing text over many lines with one print() command
print('''\n\n
This function called def direction():
asks the player to give input to indicate which direction
they want to go.
Any combination of [L  or  Left  R  or  Right] entered will
work because the function converts the input to lower case
when the user presses the Enter key.

TRY ENTERING Right using both upper and lower case letters
[ RigHT ] and it will still work.
If the player enters anything other than right or left then
the else: clause catches this and then returns them back to
the begining to try again.

Try yourself enter any combination of
[l, L, r, R, Right, right, Left, left]
Upper case, Lower case, Mixed case, it works!\n\n\n''')

# input is used here to pause the game
# input('Press Enter to continue:')   NOTE used during development
# this print command is using the newline escape characters to print
# 2 blank lines  making it easier to read the text in the console.
print('\n\n')


# this is the direction(): function
def direction():
    try:                                                   # try is the begining of the try except clause used to catch error
        left_right = input('which way [Left/Right] ')      # variable left_right assingnment statement no need to use str() as input is always in the form of a string
        left_right = left_right.lower()    # NOTE this line converts users input to lowercase
        if left_right == 'l' or left_right == 'left':      # make desion based on input
            print('Left it is then')
        elif left_right == 'r' or left_right == 'right':   # same as above this time for right
            print('Right it is then')
        else:
            print('You have to choose Left or Right you entered [', left_right, '] Please try again\n')
            sleep(1)
            direction()                         # calls the direction() function again
    except ValueError as err:                   # the except clause catches an error if there is one, and holds it in the variable call err
        print('there\'s been an error', err)    # this line then prints it out


direction()


# again this is printing 3 blank lines, but this time using *3 to repeat the newline request '\n'
print('\n' * 3)


print('''This next piece of code uses the try / except to catch an error if the user
enters anything other than a number. It catches the error using the except
clause and saves it in the varible named err.
This is then printed out so you can see what the error was

Try it out if you enter a number all is good, but if you enter anything except
the numbers [ 1 2 3 4 5 6 7 8 9 or 0 ] an error will happen and it will print
out the error captured by the variable named err''')

# piece of code to print out what the error was.
# when using try / except the line <except ValueError as err:> catches the error and stores it in the variable err
# the error is then printed out with the line <print(err)> showing you what the error was
# TRY IT WHEN ASKED DON'T ENTER A NUMBER ENTER A LETTER OR A NAME #
try:
    num = int(input('Enter a number: '))
    print('Your number was ', num)
except ValueError as err:
    print('\n\n\nyou made an error')
    print(err, '\n')
    input('Hit Enter to continue...')

print('''\n\n
This next function called yes_or_no forces the player to enter Yes or No
If anything other than [ y, Y, yes, Yes, n, N, no, No] is entered then
the player is advised of their error and asked to try again.
Once again Yes and No can be entered in mixed case ie: yEs will work\n''')

# function to make the player choose Yes or No
def yes_or_no():
    try:
        yes_no = input('Enter Yes or No ')
        yes_no = yes_no.lower()
        if yes_no == 'y' or yes_no == 'yes':
            print('You chose Yes')
        elif yes_no == 'n' or yes_no == 'no':
            print('You chose No')
        else:
            print('You have to choose either Yes or No')
            print('You have entered [ {} ]'.format(yes_no))
            yes_or_no()
    except:  # NOTE except is left bare here to catch all errors
        print('An error has occured')


yes_or_no()

sleep(1)
print('\nFinished Have a Great Day - see you soon\n\n')
