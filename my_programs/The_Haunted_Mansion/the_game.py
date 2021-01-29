#Here is where we will write the main code for our game!
#Starting with Mika's intro and then moving into the different rooms ect.
#Please do no put the full code for questions.py or health.py in here, they will be stored in seperate files
#We can call those functions for now and comment it out e.g
#questions()

import function_module
import sys
from time import sleep
import webbrowser

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
    name = input("To pass into the building the spirits demand a name. Reveal your identity.\n")

play = ""
while play.lower() not in [ "yes", "y", "no", "n" ]:
    play = input(f"So... {name}... \nAre you brave enough to enter the Haunted mansion? Once you go in there is no turning back.  [Y/N] \n") 



# NOTE: Do they want to play
if play.lower() in ["yes", "y"]:
    # NOTE: Question 1

    function_module.healthbar(health)
    
    function_module.print_str("You awake in a dimly lit room, vaguely aware of a throbbing coming from somewhere deep in your head, or is it below you in the house? You push yourself up off the filthy rotting floorboards and hear the scuttle of what you hope is a rat. There is enough moonlight filtering in through the thick dusty curtains to make out what appears to be 4 doors. Each scrawled with a letter in what you hope is not blood. \n")

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
            function_module.print_str("\n Progress to the next room.\n")

        else:
            #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer("\n You twist the door handle, there is a sharp click and you swing it open. You vaguely hear a rapid clicking like an egg timer before you can locate the source of the sound you hear a loud bang from an explosion above your head. The last thing you perceive is the sound of your own skull crumpling. \n", health)
    else:
        function_module.print_str("I ran out of questions!")
        



    
    # NOTE: Question 2
    function_module.print_str('''\n Your hand trembles from the cold as you push the door open, how did it get so cold so quickly? Your breath comes quick and frosts in the air in front of you. As you progress into the next room you recognise that it is empty apart from a few old deflated footballs. Above the flickering fireplace you spot a ragged old shirt. \n \n As your eyes adjust to the dark you notice that it has been pulled over a shapeless bulk. You stumble further inside, a twitch catches your eye, you hope that it was not the bulk. You look around the room and that it is a pentagon with 4 additional doors caked in mud, grass growing in the letters A, B, C and D. You glance back up at the dancing fireplace and notice that the shirt, and the bulk are no longer there. Cautiously you move closer to the fireplace which is steadily dying. It flickers out just as you reach it and the cold descends again. \n \n Frozen, fetid breath envelops your neck before you turn around and come face to face with the mottled flesh of a young man long dead, a close-cut hairstyle now patchy. As he opens his mouth to speak bile, blood and saliva pours down his ripped football shirt. Beneath the rolling eyes his mouth moves spraying you with the disgusting liquid. Another Question! You take a step back and trip, falling backwards into the fireplace. The logs are surprisingly cold. As you push yourself up, you realise the man has vanished. Squinting, you choose a door. \n''')

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
            function_module.print_str("\n Progress to the next room. \n")
            sleep(sleep_time)
                
        else:
            #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer('''\n You open the door and step into the darkness, it slams shut behind you. You are kicked roughly from one side and then again from the other. Studs breaking your skin. You try to push back but are forced to the floor. You feel your legs and fingers break and are powerless to stop the end under the melee. Slowly the bulk from above the fireplace climbs down and pulls your smashed body out from behind the door. It kneels over and starts tearing flesh from bone before dragging your carcass into the fireplace. \n''', health)

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
    print('''\n The door swings open and you find yourself in a cramped passage. The wall ahead of you is pockmarked with strange protrusions. Looking left and right and realising that the only way is up, you gingerly extend a hand and pull yourself up, making the mistake of looking at what the hand holds are, you quickly look away realizing that the bones look a little too human. \n \n As you reach the first precipice there is a thunderous beat of colossal wings and you are pinned beneath a huge clawed foot. Looking up, you see the face and torso of a woman soaked in blood, but with the wings and legs of some gigantic bird. She regards you with a beady eye and squawks loudly as she removes her foot from your chest, you stare around wildly and spy that there are indeed 4 doors behind her each with a different letter scratched into their frame as if by claw marks. You cannot get past her. She screeches a question. You scramble towards your choice. \n''')
    sleep(sleep_time)

    function_module.door2()

    random_q = function_module.rand_question()
    if random_q >= 0:
        if function_module.question(random_q):
            #We had a question, they got it right. Put what happens next here!
            function_module.print_str("\n Progress to the next room.\n")
            sleep(sleep_time)
                
        else:
            #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer('''\n \n You fling the door open and lose your footing on soft earth. Pushing yourself upright the stench of old coffee filling your lungs. Rolling the dirt between your fingers you realise your fall has been stopped by a floor covered in used coffee grounds. You look up confused before realising you are being regarded by the same bird woman. Before you have a chance to react, she leaps into the air, crushing you beneath her talons and wastes no time burying her mouth into the back of your neck. Your last breaths are blocked by the coffee grounds filling your mouth and nostrils. \n''', health)

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
    function_module.print_str('''\n You swing the door wide as you sprint into the next room, nearly knocking yourself unconscious as you collide with a large object. Pushing yourself up you lock eyes with…. Yourself? The room looks identical at both ends, filled with the same broken glass mirrors. You realise you must be looking in one large slim mirror that sits in the centre of a wall. \n \n You look behind you and can only see the door you came in through. You look past your reflection and see 4 doors, each labelled with A, B, C or D etched into the glass. Confused, you reach out to put a hand on the mirror. With a start, you pull back realising that you came into contact not with cold glass, but warm skin. Terrified you shrink back, and then try to dart forward, colliding with your reflection and knocking both of you back. \n \n As you open your mouth to speak you are drowned out by a deep thunderous question from your doppelganger. Another question is asked. You blink once, working out the questions in your head and as soon as you open your eyes, you realise the reflection is gone. Gingerly you step through the opening where you thought the mirror was and crunch over the floor covered in broken glass. You can’t quite shake the feeling of being watched by your own reflection as you glance around. \n''')
    sleep(sleep_time)

    function_module.door3()

    random_q = function_module.rand_question()

    if random_q >= 0:
        if function_module.question(random_q):
            #We had a question, they got it right. Put what happens next here!
            function_module.print_str("Progress to the next room.")
            sleep(sleep_time)    
        else:
            #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer('''\n You reach for the handle, watching your own reflection do the same. But as your fingers touch the handle a hand, just like your own darts out from the mirror, grabbing you by the wrist and pulling you through the glass with surprising strength. You don’t even have time to scream. The room is filled with reflections of you hammering on glass, desperately trying to get out. So, absorbed in this are you, that you don’t see an angular figure approach you from behind. \n''', health)

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
    function_module.print_str('''\n You step through into the darkness and as you gingerly place your foot down to find your balance, find that there is no floor there. You start as you fall forwards, legs tumbling over your head for what seems like an age. Until finally, with a colossal splash, you land in a freezing body of water. Struggling and trashing upwards you break the surface and spit out the silty liquid. The water is cold, not the usual cold of a refreshing shower, but a deep cold, the kind that lingers and clings to your bones, slowly eroding your senses. \n \n As your eyes adjust to the darkness and you see the walls of a cave, you feel or rather sense, something very large swimming past you. \n Across the water you see a bank with a single cave entrance. Your limbs are losing feeling, so you thrash across the water trying to get towards the bay. \n \n The cave looms close but just as you feel you are making progress, a thick barbed thing wraps itself around one of your legs and pulls you under. You inhale a lungful of water and immediately regret it, spluttering and gagging. Curiously there seems to be more light underwater and you realise that is coming from one colossal eye, about the size of a house. Paralysed with fear and cold exhaustion, you stare numbly back as your mind makes peace with the inevitable. But echoing through the water you hear the words of a question, after each word there is a loud snipping as if an enormous vice is opening and snapping shut. \n''')
    sleep(sleep_time)

    function_module.door4()
    
    random_q = function_module.rand_question()
    if random_q >= 0:
        if function_module.question(random_q):
            #We had a question, they got it right. Put what happens next here!
            function_module.print_str('''\n The creature lets go of your leg and in a swirl of liquid cold plunges deep into the depths below. The kick back from the current pushes you to the surface. Seeing your chance, you flail your limbs and make it to the bay. You crawl onto the sharp and slippery rocks, cutting your hands and forearms in the process. You make it to the cave desperately panting and vomiting up water. You notice that the cave is much less deep than you initially expected, and that there is a wooden rotting door at the far end. You push through it. \n''')
                
        else:
            #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer('''\n You feel the barbs cut deeper into the flesh of your leg as the creature tenses. A deep sense of foreboding washes over you as you are pulled deeper underwater and through a mass of tentacles. You look up and at the last moment see a huge beak snapping open and shut. The water clouds with your blood.\n ''', health)

    else:
        function_module.print_str("I ran out of questions!")



    # NOTE: Question 6
    function_module.print_str('''\n The new room is warm and bright. Initially blinded you see that you are in a cave lit by many torches. Squinting in the brightness you see that the cave is filled with sheep looking up at you bemused, you see many cheeses hanging from the ceiling and a hill at the far end of the cave. Confused, you try to push forward through the bleating mass. After making it to the middle of the cave you become aware that one of the sheep appears to be following you. You turn and it raises its head it’s square pupils staring at you unnervingly. Dumbly it opens its mouth and bleats the question. \n''')
    sleep(sleep_time)

    function_module.door5()

    random_q = function_module.rand_question()
    if random_q >= 0:
        if function_module.question(random_q):
            #We had a question, they got it right. Put what happens next here!
            function_module.print_str('''\n The sheep trots away a short distance and looks back at you as if expecting you to follow. You obligingly do so, and it leads you to a small opening hidden in the wall of the cave. You hear the sound of something large grumble nearby. Panicking the sheep gives you a shove from behind. You squeeze through the opening and continue along the passage and through the door at the end. \n''')
            sleep(sleep_time)
                
        else:
            #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer('''\n The sheep opens its mouth and lets out a scream. The mass of sheep parts and the hill, which you now realise is not a hill, slowly moves and unfurls into a giant of a man. He stands at 3 stories tall with pale white mole speckled skin. Your eyes track up his flabby body a shapeless mass of sweating folds of skin hanging loose. It takes a step towards you, it’s bulk rippling with each step. It fixes you with a single rolling eye, it's pupil constricting as it focuses on you. It crosses the room with surprising speed. Snatching you from the ground it tears off your head with teeth like tombstones. Your head is crushed between its giant molars just as your nose fills with the stench of fetid breath. \n''',health)

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
    function_module.print_str('''\n As you enter the new room you are taken aback. It looks like an old bedroom, with a ragged 4 poster bed in the centre. 4 more doors leading off from each of the walls. At the end of the bed is a freestanding faded mirror aged with time. A slim figure with its back to you is admiring its own reflection. At the sound of the door swinging shut behind you. The person turns and stares at you. You are taken aback. \n \n The person is neither male nor female, but undoubtedly the most beautiful person you have seen, he or is it she? Smiles at you with a dazzling open smile, not one of kindness or warmth but one of a tiger that has found a wounded deer wander into its lair. It walks towards you flashing that unnerving smile. \n \n As it gets closer you see that it is wearing a slim black form hugging dress or is it a suit? It catches the light and you realise its clothes are made of what looks like raven black hair. Flawless tanned skin is pulled tight around ruby red lips and vertical feline eyes. As you are frozen in fright it takes you by the hand and gently leads you closer to the bed and mirror. The creature smells metallic, like raw beef and wet iron. It sniffs as if breathing in your scent and leans forward speaking in a low growling hungry voice. \n''')

    function_module.door6()

    random_q = function_module.rand_question()

    if random_q >= 0:
        if function_module.question(random_q):
    #We had a question, they got it right. Put what happens next here!
            function_module.print_str('''\n The creature sniffs again in disappointment and turns away from you leaping cat like onto its bed. It walks on top of the covers in a circle, keeping you in its gaze before curling up into a ball and yawning loudly, showing far too many pointed teeth. It closes its eyes, but you notice a tiny glimmer under its eyelids and realise the creature is still watching you. You turn and run towards your door of choice. \n''')
        else:
    #They got the answer wrong, put consequences here!
            health = function_module.wrong_answer('''\n The creature’s eyes light up and it rolls it’s head on its shoulders baring its many pointed teeth. You turn and run toward your door of choice, but the creature merely looks at you patiently. As you reach your chosen door you turn the handle and pull realising it is locked. You wheel around just in time to see the creature land on top of you and bury its head in your neck. Your gurgling screams are mixed with the creature's snarls. It tears at your throat, and then, silence. \n''', health)
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
    function_module.print_str('''\n You slam the door closed behind you panting and slide to the floor, what fresh horror would await you in this room? You are surprised to find that it is well lit by torches with a solitary figure sat at the end of a table piled high with food. Around the table, set into the walls are 4 doors labelled with beautiful motifs A, B, C and D. You sit staring and panting for a moment and when you see that the figure does not move you get up and approach the table.\n \n Eyes fixed on the figure, you notice it is a hooded individual shrouded in a black robe, almost monkish. It has a thin, skeletal frame. You sit at the table as far away from the figure as possible and reach forward to take an apple. Still the figure does not move. You bite into the apple as slowly and as quietly as possible. It is delicious, it is the most delicious piece of food that you have ever eaten. The juice of the apple runs down your throat and you hungrily bite into another piece. \n \n You eat it, core and all. Your eyes set on a roast chicken and you rip off a leg. The skin is beautifully golden and crispy flavoured with herbs, garlic and pepper. Finishing one leg and then another you dig into the flesh of the breast with your teeth, the skin crackling sounding like a melody to your ears and the soft meat tearing away.Then the torches go out. \n \n Before you can realise what has happened, the torches blaze again and the table is filled by more shrouded figures. With a start you drop the chicken and try to stand up before being roughly shoved back into your seat. You sob and try to apologise and and stand but the figures remain silent. One pushes you down from behind while the two either side of you grasp your arms with frightening strength from their bony fingers. All the figures lean in towards you and rasp a question. \n''')

    function_module.door7()

    random_q = function_module.rand_question()

    if random_q >= 0:
        if function_module.question(random_q):
    #We had a question, they got it right. Put what happens next here!
            function_module.print_str('''\n The figures release their grip and you scramble away apologising. The figure stood behind you takes its seat at the table and the shrouded congregation sits in silence in front of the food. You run towards the door of your choice and don’t look back. You turn and run towards your door of choice. \n''')
        else:
    #They got the answer wrong, put consequences here!
            function_module.wrong_answer('''\n the figures pull back their hoods and you see that they are gaunt figures, with skin stretched thinly over bone. But they have no eyes. Instead two black lifeless holes caked in dried blood stare out. The two figures lift you up by your arms and throw you onto the table. A mania descends over the gaunt congregation and they all grasp forwards to your body, pulling you spread eagle, tearing off one leg and then another. They clamber up onto the table and dig into your torso with their teeth, piercing the skin and digging into your flesh. \n''', health)
    else:
        function_module.print_str("I ran out of questions!")




    # NOTE:Question 9
    function_module.print_str('''\nYou barge in through the door and slip and fall on a polished wood floor. You shake your head in disbelief the floor panels are spotless and tessellated. You look up and see a concerned face staring down at you. It is a man; he appears to be around 40 years old with slicked back hair and generous features. He extends a hand which you take. He is wearing a slim fitting black suit that you notice is slightly frayed at the seams with a crisp white shirt underneath. On closer inspection however several buttons are missing. His shoes are polished to a mirror shine, but you can still see the cracks in the leather. Not wishing to cause offense you reach up and take the hand. He pulls you in close and you both begin to dance a slow waltz. Music filters the room from somewhere and looking wildly about you notice 4 doors in ornate mahogany labelled in faded gold lettering A,B,C and D. You try and move your feet in time with the music as he smiles at you and asks.  \n''')

    function_module.door9()

    random_q = function_module.rand_question()

    if random_q >= 0:
        if function_module.question(random_q):
    #We had a question, they got it right. Put what happens next here!
            function_module.print_str('''\n The man nods very slightly, his smile remaining fixed and your dance comes to an end. He bows and gestures towards your door of choice. You thank him and walk through the door relieved.  \n''')
        else:
    #They got the answer wrong, put consequences here!
            function_module.wrong_answer('''\n The man’s smile vanishes and is replaced by a frown. The music and the dance speed up and you desperately try to keep pace, but the man’s arms tighten around your already exhausted frame and he drags you across the floor. The music and the dance get faster and faster. Your legs give way like jelly, you try to push away from his vice like grasp and but he moves faster and faster, impossibly fast and you pass out, unable to keep pace. The man keeps moving and your shoes slowly wear away and then the skin of your feet and then the flesh and then the bone. The man does not stop until you are dust in his arms. Once that has blown away, he bows, and a smile returns to his face. \n''', health)
    else:
        function_module.print_str("I ran out of questions!")





    function_module.door10()

    random_q = function_module.rand_question()


    if random_q >= 0:
        if function_module.question(random_q):
    #We had a question, they got it right. Put what happens next here!
            function_module.print_str('''\n She turns away from you and the feeling in your legs is restored.The bar crumbles to sand in your hand and rather than take your chances, you head through the door. \n''')
        else:
    #They got the answer wrong, put consequences here!
            function_module.wrong_answer('''\n She hisses at you again turns away. Something strikes you from above and you look up and realise that gold bars are falling from the ceiling. You rush to one of the doors and frantically try to pull it open. The woman is nowhere to be seen. A bar falls and hits you in the shoulder, shattering it. You stumble backwards as one glances off your head. Dazed you trip backwards over a stack of paper falling face up. Despite your efforts you are beaten down by the heavy bars. It is all over when a final bar slams into your face spraying blood and brain over the paper covered floor. \n''', health)
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
