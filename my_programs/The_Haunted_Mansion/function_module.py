from random import randint
import random
import webbrowser

from time import sleep
import sys

list_of_questions = [
        ['''
    What body parts do northern leopard frogs use to help swallow their prey?

    A)Feet                              B)Eyes

    C)Ears                              D)Nostrils
    ''','''
    Correct! Northern leopard frogs use their ears to help swallow their prey.
    ''','''
    Incorrect!  Northern leopard frogs use their ears to help swallow their prey.
    ''','''b''', False],

    ['''
    What colour is the solid form of oxygen?
    
    A)Red                               B)Green
    
    C)Yellow                            D)Blue
     ''','''
     Correct! The solid colour for of oxygen is infact blue.
     ''','''
     Incorrect! The solid colour for of oxygen is infact blue''','''d''', False],

     ['''
    What colour is the sunset on Mars?

    A)Red                               B)Green

    C)Blue                              D)Orange
    ''','''
    Correct! The sunset on mars is blue (And really cool!).
    ''','''
    Incorrect! The sunset on mars is blue (And really cool!).
    ''','''c''', False],

    ['''
    Which part of the human body does not have a blood supply?
    
    A) Kneecap                          B)Earlobe
    
    C)Fingernails                       D)Cornea
    ''','''
     Correct! The cornea have no blood supply!.
    ''','''
    Incorrect! The cornea have no blood supply!.
    ''','''d''', False],

    ['''
    In 2015, Merlin the rescue cat set a new world record for what?

    A)Longest Fur                       B)Loudest Purr

    C)Best Mouser                       D)Heaviest Cat
    ''','''
    Correct! The most adorable world record ever for the loudest purr.
    ''','''
    Incorrect! The most adorable world record ever for the loudest purr.
    ''','''b''', False],

    ['''
    What was William Shakespeare's last play called?

    A)The Tempest                       B)A Midsummer Night's Dream
    
    C)Romeo and Juliet                  D)As you like it
    ''','''
    Correct - Legend has it that this is the first of two plays Shakespeare wrote for a mysterious figure that gifted him his powers of writing.
    ''','''
    Incorrect!  Perhaps you should reaquaint yourself with the Bard from Stratford upon Avon.
    ''',
    '''a''', False],

    ['''
    What is the primary reason Millennials are unable to buy houses?

    A)Poor economic management and      B)Corporate greed
      policy decision making from the 
      previous generation 
    
    C)Avocados                          D)The free market
    ''','''
    Correct - Poor money management and lack of get up and go is the reason that many in the 'Millennial' generation are unable to afford houses. Other reasons include: cereal cafes, inability to open a can of beans, being a snowflake and not working as hard as the previous generation, apparently.
    ''','''
    Incorrect! Back to the Northern Quarter with you. 
    '''
    ,'''c''', False],

    ['''
    Which of the following video game franchises is the brain child of the famous director Hideo Kojima?

    A)Plastic Wrench Liquid             B)Metal Gear Solid
    
    C)Call of Duty                      D)Shout of Obligation
    ''','''
    Correct - Despite it's convoluted story and awkward name. Metal Gear Solid remains the defining franchise of the stealth genre.
    ''','''
    Incorrect - Snake what happened? Snake? SSSSSSNNNNNNNNAAAAAAAAAAAAAAAAAAKKKKKKKKKKKKKKKKKKEEEEEEEEEE!
    '''
    ,'''b''', False],

    ['''
    Which of the following US Presidents suffered from extreme stage fright?

    A)Alexander Hamilton                B)Abraham Lincoln
    
    C)Thomas Jefferson                  D)Ulysses Grant
    ''','''
    Correct - Despite his portrayal in the hit musical 'Hamilton' Thomas Jefferson only gave two speeches in his life and even then audiences had to strain to hear him. This was despite kicking ass as the ambassador to France.
    ''','''
    Incorrect - I'm afraid you will never be president, or in the room where it happens.
    '''
    ,'''c''', False],

    ['''
    Recent research suggests that dinosaurs who once ruled the planet has what kind of skin?

    A)Leathery                          B)Smooth
    
    C)Furry                             D)Feathery
    ''','''
    Correct - Recent research suggests that dinosaurs, as they were more closely related to birds were feathered. Even the fearsome T-Rex is considered to have had feathers along it's head, neck and tail. The velociraptor was about the size of a chicken and feathered as such. Clever girl...
    ''','''
    Incorrect - You have been eaten by a T-Rex.
    '''
    ,'''d''', False],

    ['''
    Who is England's all time top goal scorer?

    A)  Bobby CHarlton                  B)  Gary Lineker
    
    C)  Wayne Rooney                    D)  Alan Shearer
    ''','''
    Correct! - Wayne Rooney overtook Bobby Charlton's recored of 49 international goals on Tuesday 8th September 2015.
    ''','''
    Incorrect! - Wayne Rooney overtook Bobby Charlton's recored of 49 international goals on Tuesday 8th September 2015.
    ''',
    'c', False],

    ['''
    Who holds the record for most appearances in the Premier League?

    A)  Ryan Giggs                      B)  Gareth Barry
    
    C)  James Milner                    D)  David James
    ''','''
    Correct! - Gareth Barry holds the record after 653 career Premier League appearances for Aston Villa, Manchester City, Everton & West Brom.
    ''','''
    Incorrect! - Gareth Barry holds the record after 653 career Premier League appearances for Aston Villa, Manchester City, Everton & West Brom.
    ''',
    'b', False],

    ['''
    Who was the first person in space?

    A)  Yuri gagarin                    B) Buzz Aldrin
    
    C)  Neil Armstrong                  D) Alan Shepherd
    ''','''
    Correct! - Although Neil Armstrong was the first man on the moon and Alan Shepherd was the first American in space, Yuri Gagarin was the first person to go into space.
    ''','''
    Incorrect! - Although Neil Armstrong was the first man on the moon and Alan Shepherd was the first American in space, Yuri Gagarin was the first person to go into space.
    ''',
    'a', False],

    ['''
    Which nation has won the most World Cups?

    A)  Italy                           B) France
    
    C)  Germany                         D) Brazil
    ''','''
    Correct! - Brazil have won the most World Cups with 5, despite not winning any of the last 4 tournaments.
    ''','''
    Incorrect! - Brazil have won the most World Cups with 5, despite not winning any of the last 4 tournaments.
    ''',
    'd', False],

    ['''
    Which of these is not a metal?

    A)  Magnesium                       B) Lithium
    
    C)  Uranium                         D) Nitrogen
    ''','''
    Correct! - Nitrogen is the only element that is not a metal.
    ''','''
    Incorrect! - Nitrogen is the only element that is not a metal.
    ''',
    'd', False],

    ['''
    Who is often called the father of the computer?

    A) Eben Upton                       B)David Montgomery
    
    C) Charles Babbage                  D) William Shockley
    ''','''
    Correct! - Charles Babbage is often called the father of the computer.
    ''','''
    Incorrect! - Charles Babbage is often called the father of the computer.
    ''','''c''', False],

    ['''
    Which of these is not a seconday primary colour

    A)RED                               B)YELLOW
    
    C)CYAN                              D)MAGENTA
    ''','''
    Correct! The primary colours are RED GREEN and BLUE
             and the secondary primaries are MAGENTA CYAN and YELLOW
    ''','''
    Incorrect! The primary colours are RED GREEN and BLUE
               and the secondary primaries are MAGENTA CYAN and YELLOW
    ''','''a''', False],

    ['''
    What is the answer to this maths question 2**8

    A)256                               B)64
    
    C)1024                              D)512
    ''','''
    Correct! - 2 x 2 x 2 x 2 x 2 x 2 x 2 x2  =  256
    Two to the power of 8
    ''','''
    Incorrect! - 2 x 2 x 2 x 2 x 2 x 2 x 2 x2  =  256
    Two to the power of 8
    ''','''a''', False],
    
    ['''
    What is the middle name of Morrissey, the singer from The Smiths?

    A)Patrick                           B)Robert
    
    C)Albert                            D)Marvin
    ''','''
    Correct! - Morrisseys middle name is Patrick
    ''','''
    Incorrect! - I'm afraid the answer is Patrick.
    ''','''a''', False],

    ['''
    Who is credited with creating the first compiler for a computer programming language

    A)Grace Hopper                      B)Ada Lovelace
    
    C)Dennis Hopper                     D)Sophie Wilson
    ''','''
    Correct! - Grace Brewster Murray Hopper (née Murray December 9, 1906 – January 1, 1992) 
    was an American computer scientist and United States Navy rear admiral.[1] One of the 
    first programmers of the Harvard Mark I computer,
    ''','''
    Incorrect! - Grace Brewster Murray Hopper (née Murray December 9, 1906 – January 1, 1992) 
    was an American computer scientist and United States Navy rear admiral.[1] One of the 
    first programmers of the Harvard Mark I computer,
    ''','''a''', False]
]
spd = 0.02

def print_str( str ):
        for character in str:
            sys.stdout.write(character)
            sys.stdout.flush()
            sleep(spd)

# function which asks a question
def question(pos):
        #If the question has been asked before - exit the function; else mark it as asked before
        if list_of_questions[pos][4]:
                return
        else:
                list_of_questions[pos][4] = True

        #print("Asked question " + pos)
	# for loop prints question on the screen
        print_str(list_of_questions[pos][0])
              
        ans = input('\n\nEnter your answer here :').lower() # get answer from contestant
        while ans not in ["a", "b", "c", "d"]:  #Checks they gave an acceptable answer
                ans = input('\nTry again. Which one is the correct answer?').lower()

        if ans == list_of_questions[pos][3]:          # NOTE this line matches the correct answer in the question
                print_str(list_of_questions[pos][1]) # run if answer is correct
                return True
        else:
                print_str(list_of_questions[pos][2])  # run if answer is wrong
               
                return False



def rand_question():
        i = len(list_of_questions)*2
        random_q = random.randint(0,len(list_of_questions)-1)
        while i > 0 and list_of_questions[random_q][4]:
                random_q = random.randint(0, len(list_of_questions)-1)

        if list_of_questions[random_q][4]:
                return -1
        else:
                return random_q





def gameover():   
        print_str('''\nYou fall backwards into the abyss falling for what seems at first like an eternity but rather than speed up you seem to slow down until you are gently laid in a heap. You breathe but cannot distinguish where the air, if there is any air, begins and your body ends. You pick yourself up and find that you are intact, with no bruises or scars. You look down and find yourself naked, but you are not embarrassed or ashamed. You feel comfortable, as if in a warm bath. \n \n You walk forward, trying to find the walls of the blackness, but find nothing. Your eyes never seem to adjust, and you wonder how you can see your body below you, but nothing else. You walk for what might be a day or only a minute, there is no way for you to tell. Faintly you hear running water and walk towards the sound of the source. You come to a river with a fast-flowing current. It is wide, too wide to cross by swimming. Out of the darkness melts a small boat paddled by a figure with a single oar. \n \n As it draws closer you see that it is in fact a hooded skeleton. You are not afraid, however. The small boat comes to shore and the man stays still, his oar on the bank ready to push off. You obligingly step on board, more by instinct, as if you have been waiting for this journey for a long time. Once settled in the boat, the figure pushes off. You look only forward to your destination and the world dissolves away into half remembered stories.\n''')

        print("\n               ('-.     _   .-')       ('-.                           (`-.      ('-.  _  .-')   ")
        print("              ( OO ).-.( '.( OO )_   _(  OO)                        _(OO  )_  _(  OO)( \( -O )  ")
        print("  ,----.      / . --. / ,--.   ,--.)(,------.       .-'),-----. ,--(_/   ,. \(,------.,------.  ")
        print(" '  .-.('-.   | \-.  \  |   `.'   |  |  .---'      ( OO'  .-.  '\   \   /(__/ |  .---'|   /`. ' ")
        print(" |  |_( OO ).-'-'  |  | |         |  |  |          /   |  | |  | \   \ /   /  |  |    |  /  | | ")
        print(" |  | .--, \ \| |_.'  | |  |'.'|  | (|  '--.       \_) |  |\|  |  \   '   /, (|  '--. |  |_.' | ")
        print("(|  | '. (_/  |  .-.  | |  |   |  |  |  .--'         \ |  | |  |   \     /__) |  .--' |  .  '.' ")
        print(" |  '--'  |   |  | |  | |  |   |  |  |  `---.         `'  '-'  '    \   /     |  `---.|  |\  \  ")
        print("  `------'    `--' `--' `--'   `--'  `------'           `-----'      `-'      `------'`--' '--' ")

        print("\n Credits - Fahad, George, Phil, Mika and Kelsey! \n")
    
        sleep(8)
        webbrowser.open('https://www.youtube.com/watch?v=Fe93CLbHjxQ')
        
        print("The game will now end!")
        sleep(8)
        sys.exit(0)


 # NOTE: Todo : Remove hard coded 5 into a variable. prints the healthbar.
def healthbar(health):
    healthno = int(health)
    healthminus = int(5 - healthno)
    print("\n Your health is: " + healthno*'[X] ' + healthminus*'[ ]' + "\n")     

#This condenses the wrong answer code and makes it consistent across the code. 
def wrong_answer( resp, health ):
        sleep_time = 2
           #They got the answer wrong, put consequences here!
        sleep(sleep_time)
        print_str( resp )
        sleep(sleep_time)
        health -= 1
        healthbar(health)
        if health == 0:
                gameover()
        return health


def wiper():
    print('\n' * 100)

def game_win():
    # text to screen
    print_str('''\n You open the door and are blinded by the light. Squinting you step out of the building and a fresh gust of air fills your lungs. Night is turning to day, and as your eyes adjust you see the light slanting through the trees, filtering out the darkness from the night before. Somewhere a bird bursts into raucous song. You look up and see the reassuring blue of a cloudless sky. The wind rustles the trees and the air warms sympathetically. No more questions, no more monsters. You step out onto the long unkept grass and watch the grasshoppers leap away. The building once looming monstrously large and forbidding behind you, takes on a much meeker stance. Like an old abusive parent now withered down with age. Cataract windows staring out like unseeing eyes. Cracks in the brick work like wrinkles tracing their way across the façade of respectability. Odd patches of mould and ivy darkening the facade like liver spots and errant growths of hair. The smell of decay and dust, the smell of waiting to be condemned. The building creaks and grumbles with unease at the things it houses. You walk away free into the wood warmed by the rising sun.\n    ''')


    # wait 5 seconds
    sleep(10)

    # clear screen
    wiper()

    print("         +-+      +")
    print("           | +-+  |   +-+")
    print("     +-+   |   |  |   |    +--+")
    print("       |   |   |  |   |    |")
    print("       |   |   |  |   |    |")
    print("   +---+---+---+--+---+----+----+")
    print("   |                            |")
    print("   |   +-------+     +-------+  |")
    print("+--+   |       |     |       |  +--+")
    print("|  |   |       |     |       |  |  |")
    print("|  |   |    +--+     |    +--+  |  |")
    print("+--+   |    |--|     |    |--|  +--+")
    print("   |   +-------+     +-------+  |")
    print("   |             +-+            |")
    print("   |             | |            |")
    print("   |             +-+            |")
    print("   |  +--+               +--+   |")
    print("   |    +-----------------+     |")
    print("   |                            |")
    print("   +----------------------------+")
    print("")

    sleep(1)

    print("\n Thank you for playing our game! \n")
    print("\n Credits - Fahad, George, Phil, Mika and Kelsey! \n")

    sleep(1)

    # launch youtube vid
    webbrowser.open("https://www.youtube.com/watch?v=JYy69qOJWoM")



def door1():
    print("\n    Door A         Door B         Door C         Door D")
    print("  __________     __________     __________     __________   ")
    print(" |  __  __  |   |  __  __  |   |  __  __  |   |  __  __  |  ")
    print(" | |  ||  | |   | |. ||  | |   | | .||  | |   | |  || .| |  ")
    print(" | |  ||  | |   | | .||  | |   | | .||  | |   | |{ ||. | |  ")
    print(" | |__||__| |   | |__||__| |   | |__||__| |   | |__||__| |  ")
    print(" |  __{ __()|   |  __ .__()|   |  __  __()|   |  __. __()|  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |. ||  | |  ")
    print(" | |  ||{ | |   | |{ ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | | }||  | |   | | .||  | |   | | .||  | |   | |  ||. | |  ")
    print(" | |. ||  | |   | |  ||  | |   | |  || .| |   | |. ||  | |  ")
    print(" | |__||__| |   | |__||__| |   | |__||__| |   | |__||__| |  ")
    print(" |__________|   |__________|   |__________|   |__________|  \n")


def door2():
    print("\n    Door A         Door B         Door C         Door D")
    print("  __________     __________     __________     __________   ")
    print(" |  ______  |   |  ______  |   |  ______  |   |  ______  |  ")
    print(" | |......| |   | |......| |   | |......| |   | |......| |  ")
    print(" | |......| |   | |......| |   | |......| |   | |......| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" |        ()|   |   .    ()|   |        ()|   |  .     ()|  ")
    print(" |       .  |   |       .  |   |          |   |          |  ")
    print(" |.         |   |    .     |   | .        |   |       .  |  ")
    print(" |          |   |          |   |      .   |   |    .     |  ")
    print(" |  .       |   | .        |   |          |   |          |  ")
    print(" |        . |   |      .   |   |     .    |   |  .    .  |  ")
    print(" |__________|   |__________|   |__________|   |__________|  \n")


def door3():
    print("\n    Door A         Door B         Door C         Door D")
    print("  __________     __________     __________     __________   ")
    print(" |  ______  |   |  ______  |   |  ______  |   |  ______  |  ")
    print(" | |......| |   | |......| |   | |......| |   | |......| |  ")
    print(" | |......| |   | |......| |   | |......| |   | |......| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" |        ()|   |        ()|   |        ()|   |        ()|  ")
    print(" |          |   |          |   |          |   |          |  ")
    print(" |          |   |          |   |          |   |          |  ")
    print(" |          |   |          |   |          |   |          |  ")
    print(" |__________|   |__________|   |__________|   |__________|  ")
    print(" |          |   |          |   |          |   |          |  ")
    print(" |__________|   |__________|   |__________|   |__________|  \n")


def door4():
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


def door5():
    print("\n    Door A         Door B         Door C         Door D")
    print("  __________     __________     __________     __________   ")
    print(" |  __  __  |   |  __  __  |   |  __  __  |   |  __  __  |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |__||__| |   | |__||__| |   | |__||__| |   | |__||__| |  ")
    print(" |  __  __-¬|   |  __  __-¬|   |  __  __-¬|   |  __  __-¬|  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |__||__| |   | |__||__| |   | |__||__| |   | |__||__| |  ")
    print(" |__________|   |__________|   |__________|   |__________|  \n")


def door6():
    print("\n    Door A         Door B         Door C         Door D")
    print("  __________     __________     __________     __________   ")
    print(" |  ______  |   |  ______  |   |  ______  |   |  ______  |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______-¬|   | |______-¬|   | |______-¬|   | |______-¬|  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" |__________|   |__________|   |__________|   |__________|  \n")


def door7():
    print("\n    Door A         Door B         Door C         Door D")
    print("  __________     __________     __________     __________   ")
    print(" |  ______  |   |  ______  |   |  ______  |   |  ______  |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______|0|   | |______|0|   | |______|0|   | |______|0|  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" | |______| |   | |______| |   | |______| |   | |______| |  ")
    print(" |__________|   |__________|   |__________|   |__________|  \n")



def door8():
    print("\n       Door A                Door B               Door C              Door D")
    print("       ______               ______               ______               ______        ")
    print("    ,-' |  | '`-.        ,-' |  | '`-.        ,-' |  | '`-.        ,-' |  | '`-.    ")
    print("  /  |  |  |  |  \     /  |  |  |  |  \     /  |  |  |  |  \     /  |  |  |  |  \   ")
    print("  |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |   ")
    print("  |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |   ")
    print("  |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |   ")
    print("  |  |  |  |  |()|     |  |  |  |  |()|     |  |  |  |  |()|     |  |  |  |  |()|   ")
    print("  |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |   ")
    print("  |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |   ")
    print("  |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |   ")
    print("  |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |   ")
    print("  |__|__|__|__|__|     |__|__|__|__|__|     |__|__|__|__|__|     |__|__|__|__|__|   \n")


def door9():
    print("\n       Door A                Door B               Door C              Door D")
    print("       ______               ______               ______               ______        ")
    print("    ,-' |  | '`-.        ,-' |  | '`-.        ,-' |  | '`-.        ,-' |  | '`-.    ")
    print("  /  |  |  |  |  \     /  |  |  |  |  \     /  |  |  |  |  \     /  |  |  |  |  \   ")
    print("  |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |   ")
    print("  |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |   ")
    print("  |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |   ")
    print("  |  |  |  |  |()|     |  |  |  |  |()|     |  |  |  |  |()|     |  |  |  |  |()|   ")
    print("  |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |   ")
    print("  |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |     |  |  |  |  |  |   ")
    print("  |__|__|__|__|__|     |__|__|__|__|__|     |__|__|__|__|__|     |__|__|__|__|__|   ")
    print("  |              |     |              |     |              |     |              |   ")
    print("  |______________|     |______________|     |______________|     |______________|   \n")


def door10():
    print("\n       Door A                Door B               Door C              Door D")
    print("       _______               _______               _______                _______       ")
    print("    ,-' |   | '`-.        ,-' |   | '`-.        ,-' |   | '`-.        ,-' |   | '`-.    ")
    print("  /  |  |___|  |  \     /  |  |___|  |  \     /  |  |___|  |  \     /  |  |___|  |  \   ")
    print("  |  |  |_|_|  |  |     |  |  |_|_|  |  |     |  |  |_|_|  |  |     |  |  |_|_|  |  |   ")
    print("  |  |  |_|_|  |  |     |  |  |_|_|  |  |     |  |  |_|_|  |  |     |  |  |_|_|  |  |   ")
    print("  |  |  |   |  |  |     |  |  |   |  |  |     |  |  |   |  |  |     |  |  |   |  |  |   ")
    print("  |  |  |   |  |()|     |  |  |   |  |()|     |  |  |   |  |()|     |  |  |   |  |()|   ")
    print("  |  |  |   |  |  |     |  |  |   |  |  |     |  |  |   |  |  |     |  |  |   |  |  |   ")
    print("  |  |  |   |  |  |     |  |  |   |  |  |     |  |  |   |  |  |     |  |  |   |  |  |   ")
    print("  |__|__|___|__|__|     |__|__|___|__|__|     |__|__|___|__|__|     |__|__|___|__|__|   ")
    print("  |               |     |               |     |               |     |               |   ")
    print("  |_______________|     |_______________|     |_______________|     |_______________|   \n")

