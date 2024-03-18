def boss_3():

        global win_var

        import random
        import player_core
        import asciiART
        import time

        # player_core.classes()

        asciiART.LastBoss()
        print("At last, the final champion approaches. \nThose in the past who approached have fallen.\nConfidence alone won't prevail.")
        print("'Joker the Slayer' approaches quickly!\n")


        player_health = 100

        boss_health = 200

        while player_health > 0 and boss_health > 0:

            boss_roll = random.randint(1,20)

            player_roll = random.randint(10,20)

            crit_roll = random.randint (1,5)

            print(player_roll)
            print(str(boss_roll))

            if player_roll == 20:
                crit = True
                if player_core.player_class == "wizard":
                    wizard_status = True
                    player_health = player_health + 10
                    

                elif player_core.player_class == 'warrior':
                    warrior_status = True
                    player_roll = player_roll + crit_roll
                    

            else:
                crit = False
                wizard_status = False
                warrior_status = False
            if player_roll < boss_roll:
                player_health = player_health - boss_roll
                print("Boss attacks and deals "+ str(boss_roll)+" damage.\nYou now have "+ str(player_health) +" health!\n")

            elif player_roll == boss_roll:
                print("I applaud you, to be able to cancel out an attack like that requires an unnerving will.\n")

            elif player_roll > boss_roll:
                boss_health = boss_health - player_roll
                if crit == True:
                    if warrior_status == True:
                        print("You channel your warrior spirit and swing your mighty sword...CRITICAL HIT!")
                    if wizard_status == True:
                        print("You waive your staff and magic courses through your veins inundating the cave with glorious light...you gain 10 health back!")
                print("You did "+ str(player_roll) +" damage!")
                print("Boss Health: " + str(boss_health)+"\n")
                print("Your Health: "+str(player_health))
                

        if player_health > boss_health:
            print("\nYou alone have achieved Enlightenment. You alone stand at the top.\n                         You have conquered the dungeon.")
            asciiART.GameWin()
        else:
            print('You are the fallen, the one who stood no chance.')
            # print("Game Over!")
            asciiART.GameOver()

