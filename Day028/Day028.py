import random, os, time

def rollDynaDie(sides):
  roll = random.randint(1, sides)
  return roll

def getHealth():
  health = ((rollDynaDie(6)*rollDynaDie(12))/2) + 10
  return health

def getStrength():
  strength = ((rollDynaDie(6)*rollDynaDie(8))/2) + 12
  return strength

def getDamage(winnerStr, loserStr):
  damage = abs(winnerStr - loserStr) + 1
  return damage

roundCount = 0

print("⚔️ BATTLE TIME ⚔️")

player1name = input("What is the first character's name?: ")
player1class = input("What is the character type (Human, Elf, Wizard, Orc)?: ")
player1health = getHealth()
player1str = getStrength()

print()
print(player1name)
print("Health: ", player1health)
print("Strength: ", player1str)
print()

print("Who are they battling?")
print()

player2name = input("What is the second character's name?: ")
player2class = input("What is the character type (Human, Elf, Wizard, Orc)?: ")
player2health = getHealth()
player2str = getStrength()

print()
print(player2name)
print("Health: ", player2health)
print("Strength: ", player2str)
print()

time.sleep(5)
os.system("clear")

print("The battle begins!")

while player1health > 0 and player2health > 0:

  print("⚔️ BATTLE TIME ⚔️")
  roundCount += 1

  p1roll = rollDynaDie(6)
  p2roll = rollDynaDie(6)

  if p1roll > p2roll:
    tempDamage = getDamage(player1str, player2str)
    player2health = player2health - tempDamage
    print(player1name, " wins round ", roundCount)
    print(player2name, " takes a hit, with ", tempDamage, " damage")
  elif p2roll> p1roll:
    tempDamage = getDamage(player2str, player1str)
    player1health = player1health - tempDamage
    print(player2name, " wins round ", roundCount)
    print(player1name, " takes a hit, with ", tempDamage, " damage")
  else:
    print("This round battled to a draw!")

  print()
  print(player1name)
  print("Health: ", player1health)
  print()
  print(player2name)
  print("Health: ", player2health)
  print()

  if player1health < 0:
    print("Oh no, ", player1name, " has fallen!")
    print()
    print(player2name, " destroyed ", player1name, " in ", roundCount, " rounds!")
    break
  elif player2health < 0:
    print("Oh no, ", player2name, " has fallen!")
    print()
    print(player1name, " destroyed ", player2name, " in ", roundCount, " rounds!")
    break
  else:
    print("And they're both standing for the next round!")
    time.sleep(5)
    os.system("clear")
    continue

time.sleep(5)
os.system("clear")
exit()
