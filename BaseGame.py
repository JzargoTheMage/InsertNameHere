#!/usr/bin/env python
filler = 0
playerName = ""
Area = 0
Health = 0
Attack = 0
Defense = 0
Speed = 0
enemyHealth = 0
enemyAttack = 0
enemyDefense = 0
enemySpeed = 0
damage = 0
battleAction = 0
OriginalHealth = 0
OriginalAttack = 0
OriginalDefense = 0
OriginalSpeed = 0
TempAttack = 0
TempDefense = 0
TempSpeed = 0
playerType = 0
battleStatus = "None"
enemyName = "None"
poison = False
enemyPoison = False
Coins = 15
Treasure = 0
ShopMenu = 0
Adventure = 0
playAgain = 1
battle = False

#Defined actions are below

#Battle is self-explanatory, set of commands for encounters

def Battle():
    global battleAction
    SaveStats()
    while battle == True:
        print "Enemy Name: ", enemyName
        print "Enemy Health: ", enemyHealth
        print "Your Health: ", Health
        while battleAction == 0:
            battleAction = int(raw_input("Enter 1 to attack, 2 to defend, or 3 to attack with poison.  "))
        while battleAction == 1:
            if Speed > enemySpeed:
                Attacking()
                if battleStatus == "None":
                    EnemyAttacking()
                PoisonCheck()
                battleAction = 0
            if enemySpeed > Speed:
                if battleStatus == "None":
                    EnemyAttacking()
                Attacking()
                PoisonCheck()
                battleAction = 0
        while battleAction == 2:
            Defending()
            if battleStatus == "None":
                EnemyAttacking()
            ReturnDefense()
            PoisonCheck()
            battleAction = 0
        while battleAction == 3:
            if Speed > enemySpeed:
                PoisonAttacking()
                if battleStatus == "None":
                    EnemyAttacking()
                PoisonCheck()
                battleAction = 0
            if enemySpeed > Speed:
                if battleStatus == "None":
                    EnemyAttacking()
                PoisonAttacking()
                PoisonCheck()
                battleAction = 0

#Save prebattle stats and restore them later.

def SaveStats():
    global OriginalHealth
    global OriginalAttack
    global OriginalDefense
    global OriginalSpeed
    OriginalHealth = Health
    OriginalAttack = Attack
    OriginalDefense = Defense
    OriginalSpeed = Speed
    
def ReturnStats():
    global Health
    global Attack
    global Defense
    global Speed
    Health = OriginalHealth
    Attack = OriginalAttack
    Defense = OriginalDefense
    Speed = OriginalSpeed

#Function to check for victory

def CheckVictory():
    global battleStatus
    if enemyHealth <= 0:
        battleStatus = "Victory"
        Victory()

#Function to check for defeat

def CheckDefeat():
    global battleStatus
    if Health <= 0:
        battleStatus = "Defeat"
        Defeat()

#Poisonous version of Attack and vice versa 

def PoisonAttacking():
    global enemyHealth
    global damage
    global Attack
    global OriginalAttack
    global enemyPoison
    TempAttack = Attack
    Attack /= 2
    damage = Attack - enemyDefense
    enemyHealth -= damage
    enemyPoison = True
    print playerName, "successfully poisoned the", enemyName, "!"
    print "The", enemyName, "takes", damage, "points of damage!"
    Attack = TempAttack
    damage = 0
    TempAttack = 0
    CheckVictory()

def EnemyPoisonAttacking():
    global Health
    global damage
    global enemyAttack
    global OriginalAttack
    global poison
    TempAttack = enemyAttack
    enemyAttack /= 2
    damage = enemyAttack - Defense
    Health -= damage
    poison = True
    print "The", enemyName, "successfully poisoned you!"
    print playerName, "takes", damage, "points of damage!"
    enemyAttack = TempAttack
    damage = 0
    TempAttack = 0
    CheckDefeat()

#Function for poison damage

def PoisonCheck():
    global Health
    global enemyHealth
    global poison
    if poison == True:
        Health = Health - 2
        print playerName, "is damaged by poison!"
        CheckDefeat()
    if enemyPoison == True:
        enemyHealth = enemyHealth - 2
        print "The", enemyName, "is damaged by poison!"
        CheckVictory()

#Attacking puts Attack vs. enemyDefence and vice versa
        
def Attacking():
    global enemyHealth
    global damage
    damage = Attack - enemyDefense
    NegativeDamage()
    enemyHealth = enemyHealth - damage
    print playerName, "attacks the", enemyName, "!"
    print enemyName, "takes ", damage, " points of damage!"
    CheckVictory()
    damage = 0

def EnemyAttacking():
    global Health
    global damage
    damage = enemyAttack - Defense
    NegativeDamage()
    Health = Health - damage
    print "The", enemyName, "attacks!"
    print playerName, "took ", damage, " points of damage!"
    CheckDefeat()
    damage = 0

#Defending doubles Defense in exchange for the user's attack that turn (temp.)

def Defending():
    global Defense
    global Health
    global damage
    TempDefense = Defense
    Defense = Defense * 2
    print playerName, "is guarding!"

def ReturnDefense():
    Defense = TempDefense
    TempDefense = 0

#This ensures that the user does not gain Health from being attacked
    
def NegativeDamage():
    global damage
    if damage < 0:
        damage = 0

#These are the different player classes to load upon startup. After initial load they are not used.

def Warrior():
    global Health
    global Attack
    global Defense
    global Speed
    Health = 10
    Attack = 10
    Defense = 10
    Speed = 10
    
def Knight():
    global Health
    global Attack
    global Defense
    global Speed
    Health = 10
    Attack = 10
    Defense = 15
    Speed = 5
    
def Thief():
    global Health
    global Attack
    global Defense
    global Speed
    Health = 5
    Attack = 15
    Defense = 5
    Speed = 15
    
def Berserker():
    global Health
    global Attack
    global Defense
    global Speed
    Health = 15
    Attack = 15
    Defense = 5
    Speed = 5

def OP():
    global Health
    global Attack
    global Defense
    global Speed
    Health = 50
    Attack = 50
    Defense = 50
    Speed = 50

#This is the generic nameless enemy template
#Base other enemies off of this template
    
def Bandit():
    global enemyName
    global enemyHealth
    global enemyAttack
    global enemyDefense
    global enemySpeed
    global Treasure
    enemyName = "Bandit"
    enemyHealth = 5
    enemyAttack = 5
    enemyDefense = 5
    enemySpeed = 5
    Treasure = 15

def BanditLeader():
    global enemyName
    global enemyHealth
    global enemyAttack
    global enemyDefense
    global enemySpeed
    global Treasure
    enemyName = "Bandit Leader"
    enemyHealth = 10
    enemyAttack = 10
    enemyDefense = 10
    enemySpeed = 10
    Treasure = 15

def MagmaWolf():
    global enemyName
    global enemyHealth
    global enemyAttack
    global enemyDefense
    global enemySpeed
    global Treasure
    enemyName = "Magma Wolf"
    enemyHealth = 30
    enemyAttack = 25
    enemySpeed = 40
    Treasure = 50

#This states the actions to follow for a successful battle (conditions in battle def.)
    
def Victory():
    global battle
    global playerType
    global enemyType
    global poison
    global enemyPoison
    global Area
    global Coins
    global Treasure
    print playerName, "was victorious against", enemyName, "!"
    print playername, "was awarded", Treasure, "coins!"
    Coins += Treasure
    Treasure = 0
    Area = 0
    battle = False
    playerType = 0
    enemyType = 0
    poison = False
    enemyPoison = False

#This states the actions to follow for a lost battle (conditions in battle def.)

def Defeat():
    global battle
    global playerType
    global enemyType
    global poison
    global enemyPoison
    global Treasure
    global Area
    print playername, "was defeated by", enemyName, "!"
    Area = 0
    Treasure = 0
    battle = False
    playerType = 0
    enemyType = 0
    poison = False
    enemyPoison = False

#Beginning of main program here

while playAgain == 1:
    print "Welcome!"
    while playerName == "":
        playerName = raw_input("What is your name?  ")
    while filler == 0:
        print "What class do you want to play?"
        print "Type 1 for Knight."
        print "Type 2 for Warrior."
        print "Type 3 for Thief."
        print "Type 4 for Berserker."
        playerType = int(raw_input("Well? What are you?  "))
        while playerType == 1:
            print "You chose the Knight class!"
            Knight()
            filler = 1
        while playerType == 2:
            print "You chose the Warrior class!"
            Warrior()
            filler = 1
        while playerType == 3:
            print "You chose the Thief class!"
            Thief()
            filler = 1
        while playerType == 4:
            print "You chose the Berserker class!"
            Berserker()
            filler = 1
        while playerType == 42:
            print "Cheater."
            OP()
            filler = 1
    while Area == 0:
        print "What would you like to do?"
        Area = int(raw_input("Type 1 to go shopping, or 2 to proceed on your journey.  ")
    while Area == 1:
        while ShopMenu == 0:
            print "Welcome to the shop! What would you like? Upgrades are 5 coins."
            ShopMenu = int(raw_input("1 is Health, 2 is Attack, 3 is Defense, and 4 is Speed. Type 5 to return to town center.  ")
        if ShopMenu == 1:
            Coins -= 5
            Health += 5
            if Coins < 0:
                print "You don't have enough money!"
                Coins += 5
                Health -= 5
            ShopMenu = 0
        if ShopMenu == 2:
            Attack += 5
            Coins -= 5
            if Coins < 0:
                print "You don't have enough money!"
                Coins += 5
                Attack -= 5
            ShopMenu = 0
        if ShopMenu == 3:
            Defense += 5
            Coins -= 5
            if Coins < 0:
                print "You don't have enough money!"
                Coins += 5
                Defense -= 5
            ShopMenu = 0
        if ShopMenu == 4:
            Speed += 5
            Coins -= 5
            if Coins < 0:
                print "You don't have enough money!"
                Coins += 5
                Speed -= 5
            ShopMenu = 0
        if ShopMenu == 5:
            Area = 0
            ShopMenu = 0
    while Area == 2:
        while Adventure == 0:
            print "You hear a desparate call for help, almost drowned out by screams."
            print "Approaching the source of the noise, you find a ransacked caravan with one lone survivor."
            print "The man is badly injured, with a massive gouge across his chest and an arrow stuck in his shoulder."
            print "He is fading in and out of consciousness, muttering to himself.
            print "'Bandits... ambush... g-gem..... taken.....'"
            print "Suddenly, an arrow whizzes past your head, barely missing you."
            Bandit()
            battle = True
            Battle()
            if battleStatus == "Victory":
                print "After a thorough search of the bandit, you are unable to find the gem the dying man spoke of."
                print "Disappointed, you return to town and rest up."
                ReutrnStats()
                battleStatus = "None"
                Adventure += 1
                Area = 0
            if battleStatus == "Defeat":
                print "You flee from battle and return to town to rest up."
                ReturnStats()
                battleStatus = "None"
                Area = 0
        while Adventure == 1:
            print ""
            Bandit()
            battle = True
            Battle()
