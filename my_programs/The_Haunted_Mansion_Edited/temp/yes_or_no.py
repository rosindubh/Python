# phil welsby - 28 jan 2021
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
