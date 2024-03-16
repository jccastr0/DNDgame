# wizard = +10 health on crit roll (20)
# warrior = +5 attack on crit roll (20)

#import boss_core
#ascii wizard
# with open ('artwork.txt') as file:
#     print(file.read())

import asciiART
import time
# asciiART.GameScreen()

def classes():

    global player_class

    print("\nClasses: \n")
    time.sleep(1)
    
    wizard = print("Wizard: Harnessing the power of magic allows you control over the power of vitality! On critical rolls gain back 10 health.")
    # time.sleep(3)
    # asciiART.druid()
    time.sleep(5)
    #ascii warrior
    warrior= print("\nWarrior: Channel your inner rage and conquer any foe with your mighty sword! On critical rolls get a damage boost.")
    # time.sleep(3)
    # asciiART.warrior()
    time.sleep(5)
    run=True 

    while run == True:

        class_selection = input("\nWhat class do you choose challenger? ")

        
        if class_selection.lower() == "warrior":
            print("\n*POOF*\n")
            print("A warrior is born and ready for battle!\n")
            asciiART.warrior()
            player_class = "warrior"
            run = False
            

        elif class_selection.lower() == "wizard":
            print("\n*POOF*\n")
            print("A wizard arises!\n")
            asciiART.druid()
            player_class = "wizard"
            run = False
        else:
            print("\nInteresting...however "+ class_selection +" was not a choice!")
    
    if player_class.lower() == "wizard":
        username =  input('\nWhat is your name traveler? ')
        print("\n"+username.title()+ " the wizard...hmm...may your magic guide the way.\n")
    
    elif player_class.lower() == "warrior":
        username =  input('\nWhat is your name traveler? ')
        print("\n"+username.title()+' the warrior! May your sword never become dull or your bravery waiver.\n')

    