


import random

Player_die = random.randint(0,20)
Boss_Die = random.randint(0,20)



if Player_die == 20:
    print("Critical Hit!")


boss_damage, boss_roll = Boss_Die, Boss_Die
boss_health = 150
player_health = 100
player_damage = Player_die
player_defense = Player_die // .2
#boss_damage = die + 2
boss_defense = Boss_Die // .2


#roll_win = print("You did", die, "Damage")
#roll_loss = print("You lost a turn," " BOSS did", die, "damage." )


def turn_logic():

    Player_die = random.randint(0,20)
    Boss_Die = random.randint(0,20)

    roll_win = ["You ", "rolled ", "X", " on your turn"]
    roll_loss = ["Boss ", "rolled ", "x", " on its turn"]

    roll_loss[len(roll_loss)-2] = str(Boss_Die)
    roll_win[len(roll_win)-2] = str(Player_die)

    for i in range(len(roll_loss)):
        print(roll_loss[i] , end="")
    print("")


    for i in range(len(roll_win)):
        print(roll_win[i], end="")
    print("")     


    

    
    # if Player_die > Boss_Die:
    #         print("You win the turn.")
    #         boss_health = boss_health - player_damage
    #     else:
    #         print("You lost the turn.")
    #         player_health = player_health - boss_damage


def boss_intro():

    print("You wandered into the boss floor in search of riches...")
    print("There it stood...")
    print("Waiting for a proper brawl.")
    print("YOU DARE CHALLENGE ME?!")
    # print("You rolled a", die)
    # print("BOSS rolled a", boss_roll)
   









boss_intro()








