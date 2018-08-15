#Random laser and feelings character generator
#Laser and Feelings is copyright John Harper and is licensed under a CC BY-NCSA 3.0 license
#copyright Jeff Demers under the MIT License

#PACKAGES
import random

#METHODS
def OpeningSpiel():
    print("You are the crew of the interstellar scout ship Raptor.")
    print("Your mission is to explore uncharted regions of space, deal with aliens both friendly and deadly, and defend the Consortium worlds against space dangers.")
    print("Captain Darcy has been overcome by the strange psychic entity known as Something Else, leaving you to fend for yourselves while he recovers in a medical pod.")
    print("")
    print("")
def PrintOut(heroes, ship, threat):
    seperator = "---------------"
    print("")
    print("")
    print("Heroes")
    print(seperator)
    print(*heroes, sep="\n")
    print("")
    print("The Raptor")
    print(seperator)
    print(*ship, sep="\n")
    print("")
    print("The Mission")
    print(seperator)
    print(threat)
def NumberOfHeroesInput():
    numHeroes = 0
    while numHeroes > 7 or numHeroes < 1:
        n = input("How many heroes would you like to generate (max: 7, one per role): ")
        try:
            numHeroes = int(n)
        except ValueError:
            continue
    return numHeroes
def GetHeroes(numHeroes):
    styles = ["Alien", "Android","Dangerous","Hot-Shot","Intrepid","Savvy","Sexy"]
    roles = ["Doctor","Envoy","Engineer","Explorer","Pilot","Scientist","Soldier"]
    numbers = [2,3,4,5]
    goals = ["Become Captain", "Meet Sexy Aliens", "Shoot Bad Guys", "Find New Worlds", "Solve Weird Space Mysteries", "Prove Yourself", "Keep Being Awesome"]
    arHeroes = []
    for x in range(numHeroes):
        #only allows this role once
        role = random.choice(roles)
        roles.remove(role)
        style = random.choice(styles)
        number = random.choice(numbers)
        goal = random.choice(goals)
        arHeroes.append(f'({number}) {style} {role}, Goal: {goal}')
    return arHeroes
def GetShip():
    strengths = ["Fast","Nimble","Well-Armed","Powerful Shields","Superior Senses","Cloaking Device","Fightercraft"]
    weaknesses= ["Fuel Hog","Only One Medical Pod","Horrible Circuit Breakers","Grim Reputation"]
    ar = []
    i = 0
    while i < 2:
        choice = random.choice(strengths)
        strengths.remove(choice)
        ar.append(choice)
        i+=1
    ar.append(random.choice(weaknesses))
    return ar
def GetThreat():
    threat = random.choice(["Zorgon the Conqueror","The Hive Armada","Rogue Captain","Space Pirates","Cyber Zombies","Alien Brain Worms"])
    wantsTo = random.choice(["destroy/corrupt","steal/capture","bond with","protect/empower","build/synthensize","pacify/occupy"])
    the = random.choice(["space pirate king/queen", "void crystals", "star dreadnought", "quantum tunnel", "ancient space ruin", "alien artifact"])
    whichWill = random.choice(["destroy a solar system", "reverse time", "enslave a planet", "start a war/invasion","rip a hole in reality", "fix everything"])
    return f'{threat} wants to {wantsTo} the {the} which will {whichWill}'

#MAIN
OpeningSpiel()
heroes = GetHeroes(NumberOfHeroesInput())
ship = GetShip()
threat = GetThreat()
PrintOut(heroes, ship, threat)