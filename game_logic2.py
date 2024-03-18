def boss_run():


        wizard_status = True
        warrior_status = True
        global win_var

        import random
        import player_core
        import asciiART
        import time
        import os

        player_core.classes

        global next
        
        player_health = 100

        boss_health = 50

        print("You march onwards to the darkness.")
        time.sleep(3)

        print("With every step you take, you sense a growing danger.")
        time.sleep(3)

        print("Eventually while walking through the moon-colored walls, you notice a light")
        time.sleep(3)

        print("There it was, proudly standing upright.")
        time.sleep(3)

        print("Said to be a legendary beast from the days of old")
        time.sleep(3)

        print("It takes notice of you. Prepare yourself.")
        time.sleep(3)

        print("Your first enemy:\n")
        time.sleep(3)

        asciiART.MakaTitle()
        time.sleep(3)
        asciiART.SecondBossPhaseTwo()
        print("GRAAAAAAHHHH\n")
        input("Press enter to begin...")
        os.system('cls')
        asciiART.MakaTitle()
        asciiART.SecondBossPhaseTwo()

        while player_health > 0 and boss_health > 0:

            boss_roll = random.randint(1,15)

            player_roll = random.randint(1,20)

            crit_roll = random.randint (1,5)

            print("You roll a: "+ str(player_roll))
            print("Maka the Gryphon rolls a: "+str(boss_roll)+'\n')

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
                print("Using it's bloodstained claws, it strikes! dealing "+ str(boss_roll)+" damage.")
                print("Boss Health: " + str(boss_health))
                print("Your Health: "+str(player_health)+"\n")
                input('Press enter to continue...\n')
                os.system('cls')
                asciiART.MakaTitle()
                asciiART.SecondBossPhaseTwo()
            elif player_roll == boss_roll:
                print("Swiftly gaining altitude, it streamlines towards you. You parry Maka's attack.\n")
                input("Press enter to continue...\n")
                os.system('cls')
                asciiART.MakaTitle()
                asciiART.SecondBossPhaseTwo()
            elif player_roll > boss_roll:
                boss_health = boss_health - player_roll
                if crit == True:
                    if warrior_status == True:
                        print("You channel your warrior spirit and swing your mighty sword...CRITICAL HIT!\n")
                    elif wizard_status == True:
                        print("You waive your staff and magic courses through your veins inundating the cave with glorious light...you gain 10 health back!\n")
                print("You did "+ str(player_roll) +" damage!")
                print("Boss Health: " + str(boss_health))
                print("Your Health: "+str(player_health)+'\n')
                input("Press enter to continue...\n")
                os.system('cls')
                asciiART.MakaTitle()
                asciiART.SecondBossPhaseTwo()

        if player_health > boss_health:
            next = True
            os.system('cls')
            print("\nYou have slain the evil that creeps!\n")
            time.sleep(2)
            asciiART.victory()
            time.sleep(2)
            input('Press Enter to Continue!')
            os.system('cls')
        else:
            next = False
            print('Foolish mortal...your soul is mine.')
            # print("Game Over!")
            asciiART.GameOver()


        while next == True:
                        
                        import random
                        import player_core
                        import asciiART
                        import time
                        import os
            
                        print("\nWith your new found confidence, you continue your march forward.")
                        time.sleep(3)

                        print("Although, your victory was gained swiftly, a new challenger stands before you.")
                        time.sleep(3)

                        print("You march onwards.\n")
                        time.sleep(3)
                        os.system('cls')

                        print("From the depths of the sea, the ancient one rises with the ability to gain back health on parries.")
                        time.sleep(4)
                        print("It pulls out his weapon...")
                        time.sleep(2)
                        print("THE CLARINET OF DEATH.")
                        time.sleep(2)
                        os.system("cls")
                        
                        wizard_status = True
                        warrior_status = True

                        player_health = 100

                        boss_health = 80

                        asciiART.OctowardTitle()

                        asciiART.squidward()
                        print("...")
                        time.sleep(2)

                        print("You dare walk the path of a hero?")
                        time.sleep(2)

                        print("You shall perish like the rest of them.\n")
                        time.sleep(2)

                        print("*Due to copyright laws, this is not squidward but his cousin OCTOWARD!.*\n")
                        input('Press enter to continue...')
                        os.system('cls')
                        asciiART.OctowardTitle()
                        asciiART.squidward()

                        while player_health > 0 and boss_health > 0:

                            boss_roll = random.randint(1,20)

                            player_roll = random.randint(15,20)

                            crit_roll = random.randint (1,5)

                            print("\nYou roll a: "+str(player_roll))
                            print('Octoward the Kraken rolls a: '+str(boss_roll)+'\n')

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
                                    ("The enemy is strong, his power is immense...he extends his tentacles: absorbing your life energy and severely wounding you!")
                                print("Octoward strikes, dealing "+ str(boss_roll)+" damage.\nYou now have "+ str(player_health) +" health!")
                                print("Boss Health: " + str(boss_health))
                                print("Your Health: "+str(player_health)+"\n")
                                input("Press enter to continue...\n")
                                os.system('cls')
                                asciiART.OctowardTitle()
                                asciiART.squidward()

                            elif player_roll == boss_roll:
                                boss_health = boss_health + 10
                                print("The enemy is strong...your attack is parried.\nThe enemy takes his chance to drink essence of the sea gaining 10 health!\n")
                                print("Boss Health: " + str(boss_health))
                                print("Your Health: "+str(player_health)+"\n")
                                input("Press enter to continue...\n")
                                os.system('cls')
                                asciiART.OctowardTitle()
                                asciiART.squidward()

                            elif player_roll > boss_roll:
                                boss_health = boss_health - player_roll

                                if crit == True:
                                    if wizard_status == True:
                                        print("You waive your staff and magic courses through your veins inundating the cave with glorious light...you gain 10 health back!\n")
                                    elif warrior_status == True:    
                                        print("You channel your warrior spirit and swing your mighty sword...your attack is deadly and severely wounds the enemy!\n")

                                print("You did "+ str(player_roll) +" damage!")
                                print("Boss Health: " + str(boss_health))
                                print("Your Health: "+str(player_health)+"\n")
                                input("Press enter to continue...\n")
                                os.system('cls')
                                asciiART.OctowardTitle()
                                asciiART.squidward()

                        if player_health > boss_health:
                            next = True
                            os.system("cls")
                            print("\nThe enemy's shriek pierces the air making the cave tremble...another enemy falls to your hand!\n")
                            time.sleep(2)
                            asciiART.victory()
                            time.sleep(1)
                            input('Press enter to continue!')
                            os.system('cls')
                        else:
                            os.system('cls')
                            next = False
                            # print('Dead')
                            # print("Game Over!")
                            asciiART.GameOver()


                        while next == True:


                                    import random
                                    import player_core
                                    import asciiART
                                    import time
                                    import os
                                    #health_pot = True
                                    wizard_status = True
                                    warrior_status = True

                                
                                    print("At last, the final champion approaches.")
                                    time.sleep(3)
                                    print("\nThose in the past who approached have fallen.")
                                    time.sleep(3)
                                    print("\nConfidence alone won't prevail.")
                                    time.sleep(3)
                                    print("'HellMask the Slayer' approaches quickly!\n")
                                    time.sleep(3)
                                    asciiART.HellMaskTitle()
                                    asciiART.FirstBoss()
                                    print("I will defeat you.")
                                    time.sleep(3)
                                    os.system("cls")
                                    asciiART.HellMaskTitle()
                                    asciiART.FirstBoss()

                                    # player_core.classes()

                                    player_health = 100

                                    boss_health = 200

                                    while boss_health >= 100:
                                        #player_health = 100

                                        #boss_health = 200

                                        #while boss_health >= 100:

                                            

                                            boss_roll = random.randint(1,20)

                                            player_roll = random.randint(1,20)

                                            crit_roll = random.randint (1,5)

                                            print('You roll a: '+str(player_roll))
                                            print('Hellmask the slayer rolls a: '+str(boss_roll)+'\n')

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
                                                print("Boss Health: " + str(boss_health))
                                                print("Your Health: "+str(player_health)+'\n')
                                                # if health_pot == True:
                                                #      x = input('Do you want to use Health Pot? ')
                                                #      if x.lower() == 'yes' or 'y':
                                                #         player_health = player_health + 30
                                                #         print("You have gained 30 health! You now have "+str(player_health)+' health!')
                                                #         health_pot = False
                                                #      elif x.lower() == 'no' or 'n':
                                                #         print("Health Pot stored.")
                                                input("Press enter to continue...\n")
                                                os.system('cls')
                                                asciiART.HellMaskTitle()
                                                asciiART.FirstBoss()

                                            elif player_roll == boss_roll:
                                                print("I applaud you, to be able to cancel out an attack like that, requires an unnerving will.\n")
                                                # if health_pot == True:
                                                #      x = input('Do you want to use Health Pot? ')
                                                #      if x.lower() == 'yes' or 'y':
                                                #         player_health = player_health + 30
                                                #         print("You have gained 30 health! You now have "+str(player_health)+' health!')
                                                #         health_pot = False
                                                #      elif x.lower() == 'no' or 'n':
                                                #         print('Health Pot stored.')
                                                input("Press enter to continue...\n")
                                                os.system('cls')
                                                asciiART.HellMaskTitle()
                                                asciiART.FirstBoss()

                                            elif player_roll > boss_roll:
                                                boss_health = boss_health - player_roll
                                                if crit == True:
                                                    if warrior_status == True:
                                                        print("You channel your warrior spirit and swing your mighty sword...CRITICAL HIT!\n")
                                                    if wizard_status == True:
                                                        print("You waive your staff and magic courses through your veins inundating the cave with glorious light...you gain 10 health back!\n")
                                                print("You did "+ str(player_roll) +" damage!")
                                                print("Boss Health: " + str(boss_health))
                                                print("Your Health: "+str(player_health)+'\n')
                                                # if health_pot == True:
                                                #      x = input('Do you want to use Health Pot? ')
                                                    #  if x.lower() == 'yes' or 'y':
                                                    #     player_health = player_health + 30
                                                    #     print("You have gained 30 health! You now have "+str(player_health)+'health!')
                                                    #     health_pot = False
                                                    #  elif x.lower() == 'no' or 'n':
                                                    #     print("Health Pot stored")
                                                input("Press enter to continue...\n")
                                                os.system('cls')
                                                asciiART.HellMaskTitle()
                                                asciiART.FirstBoss()
                                                
                                    print('Second phase...')
                                    time.sleep(2)
                                    print('I have underestimated you...enough of the games...')
                                    time.sleep(3)
                                    print("I'll unleash my secret ability from the hein era...")
                                    time.sleep(3)
                                    os.system('cls')
                                    asciiART.cloud()
                                    time.sleep(3)
                                    os.system('cls')
                                    asciiART.HellMaskTitle()
                                    asciiART.LastBoss()
                                    time.sleep(2)
                                    print('The boss gained the ability: Lifesteal! Every turn the boss steals 2 health from you!')
                                    input('Press enter to continue...')
                                    


                                    while player_health > 0 and boss_health > 0:
                                        
                                            boss_roll = random.randint(1,20)

                                            player_roll = random.randint(1,20)

                                            crit_roll = random.randint (1,5)

                                            print('You roll a: '+ str(player_roll))
                                            print('Hellmask rolls a: '+str(boss_roll))

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
                                                
                                                player_health = player_health - 2
                                                print("Boss attacks and deals "+ str(boss_roll)+" damage.")
                                                print("Boss Health: " + str(boss_health))
                                                print("Your Health: "+str(player_health)+'\n')
                                                # if x.lower() == 'yes' or 'y':
                                                #         player_health = player_health + 30
                                                #         print("You have gained 30 health! You now have "+str(player_health)+' health!')
                                                #         health_pot = False
                                                # elif x.lower() == 'no' or 'n':
                                                #         print("Health Pot stored.")
                                                input("Press enter to continue...\n")
                                                os.system('cls')
                                                asciiART.HellMaskTitle()
                                                asciiART.LastBoss()

                                            elif player_roll == boss_roll:
                                                print("I applaud you, to be able to cancel out an attack like that requires an unnerving will.\n")
                                                player_health = player_health - 2 
                                                # if x.lower() == 'yes' or 'y':
                                                #         player_health = player_health + 30
                                                #         print("You have gained 30 health! You now have "+str(player_health)+' health!')
                                                #         health_pot = False
                                                # elif x.lower() == 'no' or 'n':
                                                #         print("Health Pot stored.")
                                                input("Press enter to continue...\n")
                                                os.system('cls')
                                                asciiART.HellMaskTitle()
                                                asciiART.LastBoss()

                                            elif player_roll > boss_roll:
                                                boss_health = boss_health - player_roll
                                                
                                                player_health = player_health - 2 
                                                if crit == True:
                                                    if warrior_status == True:
                                                        print("You channel your warrior spirit and swing your mighty sword...CRITICAL HIT!\n")
                                                    if wizard_status == True:
                                                        print("You waive your staff and magic courses through your veins inundating the cave with glorious light...you gain 10 health back!\n")
                                                print("You did "+ str(player_roll) +" damage!")
                                                print("Boss Health: " + str(boss_health))
                                                print("Your Health: "+str(player_health)+'\n')
                                                # if x.lower() == 'yes' or 'y':
                                                #         player_health = player_health + 30
                                                #         print("You have gained 30 health! You now have "+str(player_health)+' health!')
                                                #         health_pot = False
                                                # elif x.lower() == 'no' or 'n':
                                                #         print("Health Pot stored.")
                                                input("Press enter to continue...\n")
                                                os.system('cls')
                                                asciiART.HellMaskTitle()
                                                asciiART.LastBoss()






                                    if player_health > boss_health:
                                            os.system('cls')
                                            print("\nYou alone have achieved Enlightenment. You alone stand at the top.\nYou have conquered the dungeon.")
                                            asciiART.GameWin()
                                            next = False
                                    else:
                                            os.system('cls')
                                            print('You are the fallen, the one who stood no chance.')
                                            # print("Game Over!")
                                            asciiART.GameOver()
                                            next = False
                                       