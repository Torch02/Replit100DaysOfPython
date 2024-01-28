import random, os, time

def rollDynaDie(sides):
  roll = random.randint(1, sides)
  return roll
  
def getHealth():
  health = ((rollDynaDie(6)*rollDynaDie(12))/2) + 10
  return health
  
def getStrength():
  strength = ((rollDynaDie(6)*rollDynaDie(12))/2) + 1
  return strength

while True:
  print("Character Builder:")
  
  charRace = input("What race (Human, Elf, Wizard, Orc) of character do you want to create?: ")
  namePrompt = "What would you like to name your " + charRace + "?: "
  charName = input(namePrompt)
  charHealth = getHealth()
  charStrength = getStrength()

  print(charName, "- ", charRace)
  print("Health: ", charHealth)
  print("Strength: ", charStrength)
  
  choice = input("Would you like to create a new character (y/n)?: ")
  if choice == 'y':
    time.sleep(1)
    os.system("clear")
    continue
  elif choice == 'n':
    print("May your name go down in Legend...")
    time.sleep(2)
    break
  else:
    print("I really don't understand your answer")
    time.sleep(1)
    continue

exit() 
