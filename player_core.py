# wizard = +10 health on crit roll (20)
# warrior = +5 attack on crit roll (20)

#import boss_core
#ascii wizard
# with open ('artwork.txt') as file:
#     print(file.read())

# import asciiART
# asciiART.GameScreen()

def classes():

    print("\nClasses: \n")
    wizard = print("Wizard: Harnessing the power of magic allows you control over the power of vitality! On critical rolls gain back 10 health.")
    #ascii warrior
    warrior= print("\nWarrior: Channel your inner rage and conquer any foe with your mighty sword! On critical rolls get a damage boost.")

    run=True 

    while run == True:

        class_selection = input("\nWhat class do you choose challenger? ")

        
        if class_selection.lower() == "warrior":
            print("\n*POOF*\n")
            print("A warrior is born and ready for battle!")
            player_class = "warrior"
            run = False
            

        elif class_selection.lower() == "wizard":
            print("\n*POOF*\n")
            print("A wizard arises!")
            player_class = "wizard"
            run = False
        else:
            print("\nInteresting...however "+ class_selection +" was not a choice!")


