#Here is where we will write the main code for our game!
#Starting with Mika's intro and then moving into the different rooms ect.
#Please do no put the full code for questions.py or health.py in here, they will be stored in seperate files
#We can call those functions for now and comment it out e.g
#questions()

# phil welsby - 28 jan 2021
# Game created by TEAM 4 on Codenation course 4 jan to 22 jan 2021
# Team members - Mika, Fahad, Kelsey, George and Phil (Instructor - Jay)
# This version has been edited by phil welsby.

from os import system
import function_module
import sys
from time import sleep
import webbrowser
from datetime import datetime
now = datetime.now()
time = (now.hour, now.minute, now.second)
date = (now.day, now.month, now.year)

# clear screen
system('clear')

health = 5
spd = 0.005
sleep_time = 2

print("Welcome to the Haunted Mansion.")
# NOTE: Mansion with ghost in background
print('''\n                                            .-.                           
                                          .'   `.                         
                            _____         :g g   :                        
                            )   (         : o    `.                       
                           / oOo \       :         ``.                    
                          /_______\     :             `.                  
                          |       |    :  :         .   `.                
                          |  .-.  |    :   :          ` . `.              
                          |  |~|  |     `.. :            `. ``;           
  I-I-I-I-I-I-I-I-I-I-I-I-|  |_|  |I-I-I-I-I-I-I-I-I-I-I-I-I:'            
  ).**.(~~~~~~~~~~~~~~~~~~|       |~~~~~~~~~~~~~~~~~~~).**.( `.           
 / |  | \                 |       |                  / |  | \  `.     .   
 ) |__| (                _|_.---._|_                 ) |__| (,___`;.-'    
 |______|_________________|' .-. '|__________________|______|             
 |      |  .-.  .-.       |,-|~|-,|        .-.  .-.  |      |             
 \ .    /  |~|  |~|       || | | ||        |~|  |~|  \    . /             
  )H   (   |_|  |_|       ||_|_|_||        |_|  |_|   )   H(              
  |    |                  |       |                   |    |              
  |    |                  |       |                   |    |              
  \    /   ...  ...       |_.=~=._|        ...  ...   \    /              
   ). (    |~|  |~|       |I|   |I|        |~|  |~|    ) .(               
   |H |    |_|  |_|       |I|  .|I|        |_|  |_|    | H|               
   |  |                   |I|___|I|                    |  |               
   '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'               \n''')

name = ""
while name in [""]:
#while not name:
    name = input("To pass into the building the spirits demand a name. Reveal your identity.\n")
print('Hello', name, 'Welcome\n')


def play_game():
    try:
        global play
        print('Do you wish to play The Haunted House? ')
        play = input('Enter Y/n: ')
        play = play.lower()
        if play == 'y' or play == 'yes':
            print('You chose Yes')
            return play
        elif play == 'n' or play == 'no':
            print('You chose No')
        else:
            print('You have to choose either Yes or No')
            print('You have entered [ {} ]'.format(yes_no))
            play_game()

    except:  # NOTE except is left bare here to catch all errors
#        print('An error has occured')
        play_game()
play_game()

data = open('players_data.txt', 'a')
print('DATE:', date, '     TIME:', time,'     NAME:', name, '        PLAY or NOT: ', play, file = data)
data.close()

# NOTE: Do they want to play
if play.lower() in ["yes", "y"]:
    # NOTE: Question 1

    function_module.healthbar(health)

    function_module.print_str("Question 1\n")

    sleep(sleep_time)
    print("\n    Door A         Door B         Door C         Door D")
    print("  __________     __________     __________     __________   ")
    print(" |  __  __  |   |  __  __  |   |  __  __  |   |  __  __  |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |__||__| |   | |__||__| |   | |__||__| |   | |__||__| |  ")
    print(" |  __  __()|   |  __  __()|   |  __  __()|   |  __  __()|  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |__||__| |   | |__||__| |   | |__||__| |   | |__||__| |  ")
    print(" |__________|   |__________|   |__________|   |__________|  \n")


    random_q = function_module.rand_question()

    if random_q >= 0:
        if function_module.question(random_q):
            #We had a question, they got it right. Put what happens next here!
            function_module.print_str("\n Correct progress to the next room.\n")

        else:
            #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer("\n Wrong loose a life. \n", health)
    else:
        function_module.print_str("I ran out of questions!")





    # NOTE: Question 2
    function_module.print_str('''\n Question 2 \n''')

    sleep(sleep_time)

    print("\n               .-.            .-.             .-.            .-.             .-.            .-.       ")
    print("             _/@@ \          /aa \_         _/xx \          /aa \_         _/oo \          /^^ \_     ")
    print("            ( \o  /__      __\-  / )       ( \¬  /__      __\-  / )       ( \o  /__      __\-  / )    ")
    print("  /          \/   ___)    (__/    /         \/   ___)    (__/    /         \/   ___)    (__/    /     ")
    print("  \o_        /     \        /     \         /     \        /     \         /     \        /     \     ")
    print("    \|      / george\_     / fahad \__     / phil  \_     / mika  \__     / kelsey\_     /  jay  \__  ")
    print("    /\/     \_.-.__   )    \_.-._._   )    \_.-.__   )    \_.-._._   )    \_.-.__   )    \_.-._._   ) ")
    print("    \              '-'             `-`            '-'             `-`            '-'             `-`   \n")

    function_module.door8()

    function_module.healthbar(health)

    random_q = function_module.rand_question()
    if random_q >= 0:
        if function_module.question(random_q):
            #We had a question, they got it right. Put what happens next here!
            function_module.print_str("\n Correct progress to the next room. \n")
            sleep(sleep_time)

        else:
            #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer('''\n Wrong loose a life \n''', health)

    else:
        print("I ran out of questions!")

    print("\n        .-.       ")
    print("      _/oo \      ")
    print("     ( \o  /_     ")
    print("      \/   ___)   ")
    print("      /     \     ")
    print("     / george\_   ")
    print("     \_.-._._   )  ")
    print("                \n")



    # NOTE: Question 3
    print('''\n Question 3 \n''')
    sleep(sleep_time)

    function_module.door2()

    random_q = function_module.rand_question()
    if random_q >= 0:
        if function_module.question(random_q):
            #We had a question, they got it right. Put what happens next here!
            function_module.print_str("\n Correct progress to the next room.\n")
            sleep(sleep_time)

        else:
            #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer('''\n \n Wrong loose a life \n''', health)

    else:
        function_module.print_str("I ran out of questions!")


    print("\n        .-.       ")
    print("      _/^^ \      ")
    print("     ( \o  /_     ")
    print("      \/   ___)   ")
    print("      /     \     ")
    print("     / kelsey\_   ")
    print("     \_.-._._   )  ")
    print("                \n")



    # NOTE: Question 4
    function_module.print_str('''\n Question 4 \n''')
    sleep(sleep_time)

    function_module.door3()

    random_q = function_module.rand_question()

    if random_q >= 0:
        if function_module.question(random_q):
            #We had a question, they got it right. Put what happens next here!
            function_module.print_str("Correct progress to the next room.")
            sleep(sleep_time)
        else:
            #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer('''\n Wrong loose a life\n''', health)

    else:
        function_module.print_str("I ran out of questions!")

    print("\n        .-.       ")
    print("      _/UU \      ")
    print("     ( \o  /_     ")
    print("      \/   ___)   ")
    print("      /     \     ")
    print("     / fahad \_   ")
    print("     \_.-._._   )  ")
    print("                \n")


    # NOTE: Question 5
    function_module.print_str('''\n Question 5 \n''')
    sleep(sleep_time)

    function_module.door4()

    random_q = function_module.rand_question()
    if random_q >= 0:
        if function_module.question(random_q):
            #We had a question, they got it right. Put what happens next here!
            function_module.print_str('''\n Correct progress to the next room \n''')

        else:
            #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer('''\n Wrong loose a life\n ''', health)

    else:
        function_module.print_str("I ran out of questions!")



    # NOTE: Question 6
    function_module.print_str('''\n Question 6 \n''')
    sleep(sleep_time)

    function_module.door5()

    random_q = function_module.rand_question()
    if random_q >= 0:
        if function_module.question(random_q):
            #We had a question, they got it right. Put what happens next here!
            function_module.print_str('''\n Correct progress to the next room\n''')
            sleep(sleep_time)

        else:
            #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer('''\n Wrong loose a life \n''',health)

    else:
        function_module.print_str("I ran out of questions!")

    print("\n        .-.       ")
    print("      _/xx \      ")
    print("     ( \o  /_     ")
    print("      \/   ___)   ")
    print("      /     \     ")
    print("     / phil  \_   ")
    print("     \_.-._._   )  ")
    print("                \n")


    #Note:Question 7
    function_module.print_str('''\n Question 7 \n''')

    function_module.door6()

    random_q = function_module.rand_question()

    if random_q >= 0:
        if function_module.question(random_q):
    #We had a question, they got it right. Put what happens next here!
            function_module.print_str('''\n Correct progress to the next room \n''')
        else:
    #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer('''\n Wrong loose a life \n''', health)
    else:
        function_module.print_str("I ran out of questions!")


    print("\n        .-.       ")
    print("      _/@@ \      ")
    print("     ( \o  /_     ")
    print("      \/   ___)   ")
    print("      /     \     ")
    print("     / mika  \_   ")
    print("     \_.-._._   )  ")
    print("                \n")

    # NOTE:Question 8
    function_module.print_str('''\nQuestion 8 \n''')

    function_module.door7()

    random_q = function_module.rand_question()

    if random_q >= 0:
        if function_module.question(random_q):
    #We had a question, they got it right. Put what happens next here!
            function_module.print_str('''\n Correct progress to the next room \n''')
        else:
    #They got the answer wrong, put consequences here!
            function_module.wrong_answer('''\n Wrong loose a life \n''', health)
    else:
        function_module.print_str("I ran out of questions!")




    # NOTE:Question 9
    function_module.print_str('''\nQuestion 9  \n''')

    function_module.door9()

    random_q = function_module.rand_question()

    if random_q >= 0:
        if function_module.question(random_q):
    #We had a question, they got it right. Put what happens next here!
            function_module.print_str('''\n Correct progress to the next room \n''')
        else:
    #They got the answer wrong, put consequences here!
            function_module.wrong_answer('''\n Wrong loose a life \n''', health)
    else:
        function_module.print_str("I ran out of questions!")


    #NOTE:Question 10
    function_module.print_str('''
    Everything rests on Question 10
    Get it right you win
    Get it wrong you lose \n''')
    sleep(3)
    function_module.door10()

    random_q = function_module.rand_question()


    if random_q >= 0:
        if function_module.question(random_q):
    #We had a question, they got it right. Put what happens next here!
            function_module.print_str('''\n Correct your a WINNER \n''')
        else:
    #They got the answer wrong, put consequences here!
            function_module.wrong_answer('''\n Wrong you LOSE!!! \n''', health)
    else:
        function_module.print_str("I ran out of questions!")


    function_module.wiper()

    function_module.game_win()



    # NOTE: They chose to not play.
else:

    function_module.print_str('''Don't be such a wuss! \n''')
    sleep(sleep_time)
    print("\n .-') _    ('-. .-.   ('-.           ('-.       .-') _  _ .-') _     ")
    print("(  OO) )  ( OO )  / _(  OO)        _(  OO)     ( OO ) )( (  OO) )    ")
    print("/     '._ ,--. ,--.(,------.      (,------.,--./ ,--,'  \     .'_    ")
    print("|'--...__)|  | |  | |  .---'       |  .---'|   \ |  |\  ,`'--..._)   ")
    print("'--.  .--'|   .|  | |  |           |  |    |    \|  | ) |  |  \  '   ")
    print("   |  |   |       |(|  '--.       (|  '--. |  .     |/  |  |   ' |   ")
    print("   |  |   |  .-.  | |  .--'        |  .--' |  |\    |   |  |   / :   ")
    print("   |  |   |  | |  | |  `---.       |  `---.|  | \   |   |  '--'  /   ")
    print("   `--'   `--' `--' `------'       `------'`--'  `--'   `-------'    ")

    function_module.gameover()
