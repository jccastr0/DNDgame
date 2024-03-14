import random

run = True

player_health = 20

boss_health = 20

while run == True:

    boss_roll = random.randint(1,9)

    player_roll = random.randint(1,9)

    player_health = player_health - boss_roll

    if player_health <= 0:
        print("Game Over!")
    run == False