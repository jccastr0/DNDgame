import random

player_health = 100

boss_health = 50

while player_health > 0 and boss_health > 0:

    boss_roll = random.randint(1,20)

    player_roll = random.randint(1,12)

    player_health = player_health - boss_roll

    boss_health = boss_health - player_roll
    
    print("\nBoss attacks and deals "+ str(boss_roll)+" damage.\nYou now have "+ str(player_health) +" health!")

    print("You did "+ str(player_roll) +" damage!")

    print ("Boss has " + str(boss_health)+" health!\n")

if player_health > boss_health:
    print("You win!")
else:
    print('Foolish mortal...')
    print("Game Over!")