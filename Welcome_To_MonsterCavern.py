
# import asciiART
# import player_core
# import game_logic2

def begin():
    import asciiART
    import player_core
    import game_logic2

    run = True

    asciiART.GameScreen()

    while run == True:
        
        intro_cutscene = input("\nDo you dare challenge the Monster Cavern...? ")

        if intro_cutscene.lower() == "yes":
            print("\nYou will now stare at the darkness of the abyss, but forwarned the abyss stares back...")
            run = False
        else:
            print("\n" * 100 + "Begone, you're not worthy anyways. The world was overrun with monsters...darkness has won the battle.\n")
            run = False

        if intro_cutscene.lower() == "yes":
            game_logic2.boss()











