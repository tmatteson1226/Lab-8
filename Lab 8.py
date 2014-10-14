import random
playerHealth = 100
monsterHealth = 100
punchDmg = 5
swordDmg = 10
fireballDmg = 30


print 'A monster approaches! Prepare to fight!'
print 'your current health is'
print playerHealth
print 'the monsters health'
print monsterHealth

keepGoing = True
if monsterHealth <= 0:
    keepGoing = False
elif playerHealth <= 0:
    keepGoing = False
else:
    keepGoing = True

while (keepGoing == True):
    damageByMonster = random.randint(1,35)
    print 'What attack do you wish to use?'
    print '1 - Punch. 2 - Sword. 3 - Fireball'
    userInput = int(raw_input())
    if userInput == 1:
         print 'you punched the monster for 5 damage'
         monsterHealth = monsterHealth - punchDmg
         print 'the monster has ' + str(monsterHealth) + ' health'
         print 'the monster attacked you for some damage'
         playerHealth = playerHealth - damageByMonster
         print 'you have ' + str(playerHealth) + ' health'
    elif userInput == 2:
        print 'you cut the monster for 10 damage'
        monsterHealth = monsterHealth - swordDmg
        print 'the monster has ' + str(monsterHealth) + ' health'
        print 'the monster attacked you for some damage'
        playerHealth = playerHealth - damageByMonster
        print 'you have ' + str(playerHealth) + ' health'
    elif userInput == 3:
        print 'you burned the monster for 30 damage'
        monsterHealth = monsterHealth - fireballDmg
        print 'the monster has ' + str(monsterHealth) + ' health'
        print 'the monster attacked you for some damage'
        playerHealth = playerHealth - damageByMonster
        print 'you have ' + str(playerHealth) + ' health'
                  
    if playerHealth <= 0:
        print 'you have been killed by the monster'
    elif monsterHealth <= 0:
        print 'you have successfull vanquished your foe'
        
    if monsterHealth <= 0:
        keepGoing = False
    elif playerHealth <= 0:
        keepGoing = False
    else:
        keepGoing = True
