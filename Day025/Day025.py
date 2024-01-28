import random

def rollDynaDie (sides):
  roll = random.randint(1, sides)
  return roll

print("⚔️ Character Stats Generator ⚔️")
print()

while True:
  #userSides = int(input("How many sides are on your die?: "))
  #dynaRoll = rollDynaDie(userSides)
  health = rollDynaDie(6) * rollDynaDie(8)
  name = input("Name your character: ")
  print(name,"'s health is ", health, "HP")
  
  again = input("Would you like to roll another character? (Y/N): ")
  if again == "N" or again == "n":
    break
  elif again == "Y" or again == "y":
    continue
  else:
    print("I don't understand that answer.")
    break

exit()
