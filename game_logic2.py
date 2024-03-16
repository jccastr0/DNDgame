    

def boss_1():

        global win_var

        import random
        import player_core
        import asciiART
        import time

        player_core.classes


        player_health = 100

        boss_health = 150

        while player_health > 0 and boss_health > 0:

            boss_roll = random.randint(1,15)

            player_roll = random.randint(19,20)

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
            if player_roll < boss_roll:
                player_health = player_health - boss_roll
                print("Boss attacks and deals "+ str(boss_roll)+" damage.\nYou now have "+ str(player_health) +" health!\n")

            elif player_roll == boss_roll:
                print("The enemy is strong...your attack is parried!\n")

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
            print("You have slain the evil that creeps!")
           
        else:
            print('Foolish mortal...your soul is mine.')
            print("Game Over!")
            
        
def boss_2():

            import random
            import player_core
            import asciiART
            import time

            player_health = 100

            boss_health = 150

            while player_health > 0 and boss_health > 0:

                boss_roll = random.randint(1,20)

                player_roll = random.randint(1,20)

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
                    
                if boss_roll == 20:

                    boss_crit = True

                    boss_roll = boss_roll + 2

                    boss_health = boss_health + 5
                else:
                    boss_crit = False       

                if player_roll < boss_roll:
                    player_health = player_health - boss_roll
                    if boss_crit == True:
                        ("The enemy is strong his power is immense...he extends his hands and absorbs your life energy and severely wounds you!")
                    print("Boss attacks and deals "+ str(boss_roll)+" damage.\nYou now have "+ str(player_health) +" health!")
                    print("Boss Health: " + str(boss_health))
                    print("Your Health: "+str(player_health)+"\n")

                elif player_roll == boss_roll:
                    boss_health = boss_health + 10
                    print("The enemy is strong...your attack is parried and the enemy takes his chance to cast a spell and gain health!")
                    print("Boss Health: " + str(boss_health))
                    print("Your Health: "+str(player_health)+"\n")

                elif player_roll > boss_roll:
                    boss_health = boss_health - player_roll

                    if crit == True:
                        if wizard_status == True:
                            print("You waive your staff and magic courses through your veins inundating the cave with glorious light...you gain 10 health back!")
                        if warrior_status == True:    
                            print("You channel your warrior spirit and swing your mighty sword...your attack is deadly and severely wounds the enemy!")

                    print("You did "+ str(player_roll) +" damage!")
                    print("Boss Health: " + str(boss_health))
                    print("Your Health: "+str(player_health)+"\n")
                    

            if player_health > boss_health:
                print("The enemy's shriek pierces the air making the cave tremble...another enemy falls to your hand!")
            else:
                print('Foolish mortal...your soul is mine.')
                print("Game Over!")

