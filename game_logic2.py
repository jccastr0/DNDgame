def boss_run():


        wizard_status = True
        warrior_status = True
        global win_var

        import random
        import player_core
        import asciiART
        import time

        player_core.classes

        global next
        
        player_health = 100

        boss_health = 150

        while player_health > 0 and boss_health > 0:

            boss_roll = random.randint(1,15)

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
                warrior_status = False
                wizard_status = False
                
            if player_roll < boss_roll:
                player_health = player_health - boss_roll
                print("Boss attacks and deals "+ str(boss_roll)+" damage.")
                print("Boss Health: " + str(boss_health)+"\n")
                print("Your Health: "+str(player_health))
                input('Press enter to continue...')

            elif player_roll == boss_roll:
                print("The enemy is strong...your attack is parried!\n")
                input("Press enter to continue...")

            elif player_roll > boss_roll:
                boss_health = boss_health - player_roll
                if crit == True:
                    if warrior_status == True:
                        print("You channel your warrior spirit and swing your mighty sword...CRITICAL HIT!")
                    if wizard_status == True:
                        print("You waive your staff and magic courses through your veins inundating the cave with glorious light...you gain 10 health back!")
                print("You did "+ str(player_roll) +" damage!")
                print("Boss Health: " + str(boss_health))
                print("Your Health: "+str(player_health))
                input("Press enter to continue...")
                

        if player_health > boss_health:
            next = True
            print("\nYou have slain the evil that creeps!\n")
           
        else:
            next = False
            print('Foolish mortal...your soul is mine.')
            print("Game Over!")


        while next == True:
                        
                        import random
                        import player_core
                        import asciiART
                        import time

                        
                        wizard_status = True
                        warrior_status = True

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
                                input("Press enter to continue...")

                            elif player_roll == boss_roll:
                                boss_health = boss_health + 10
                                print("The enemy is strong...your attack is parried and the enemy takes his chance to cast a spell and gain health!")
                                print("Boss Health: " + str(boss_health))
                                print("Your Health: "+str(player_health)+"\n")
                                input("Press enter to continue...")

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
                                input("Press enter to continue...")

                        if player_health > boss_health:
                            next = True
                            print("\nThe enemy's shriek pierces the air making the cave tremble...another enemy falls to your hand!\n")
                        else:
                            next = False
                            print('Dead')
                            print("Game Over!")


                        while next == True:


                                    import random
                                    import player_core
                                    import asciiART
                                    import time

                                    wizard_status = True
                                    warrior_status = True

                                    # player_core.classes()

                                    asciiART.LastBoss()
                                    print("At last, the final champion approaches. \nThose in the past who approached have fallen.\nConfidence alone won't prevail.")
                                    print("'Joker the Slayer' approaches quickly!\n")


                                    player_health = 100

                                    boss_health = 200

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
                                        if player_roll < boss_roll:
                                            player_health = player_health - boss_roll
                                            print("Boss attacks and deals "+ str(boss_roll)+" damage.")
                                            print("Boss Health: " + str(boss_health)+"\n")
                                            print("Your Health: "+str(player_health))
                                            input("Press enter to continue...")

                                        elif player_roll == boss_roll:
                                            print("I applaud you, to be able to cancel out an attack like that requires an unnerving will.\n")
                                            input("Press enter to continue...")

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
                                            input("Press enter to continue...")
                                            

                                    if player_health > boss_health:
                                        print("\nYou alone have achieved Enlightenment. You alone stand at the top.\n                         You have conquered the dungeon.")
                                        asciiART.GameWin()
                                    else:
                                        print('You are the fallen, the one who stood no chance.')
                                        # print("Game Over!")
                                        asciiART.GameOver()
