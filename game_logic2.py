def boss():

    import random
    import player_core

    player_core.classes()

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
                
                player_health = player_health + 10
                

            elif player_core.player_class == 'warrior':
                
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
                print("You channel your warrior spirit and swing your mighty sword...CRITICAL HIT!")
            print("You did "+ str(player_roll) +" damage!")
            print("Boss Health: " + str(boss_health)+"\n")
            print("Your Health: "+str(player_health))
            

    if player_health > boss_health:
        print("You have slain the evil that creeps!")
    else:
        print('Foolish mortal...your soul is mine.')
        print("Game Over!")

