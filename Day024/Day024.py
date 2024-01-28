import random

def rollDynaDie (sides):
  roll = random.randint(1, sides)
  print("You rolled a ", roll)

print("Infinity Dice")
print()

while True:
  userSides = int(input("How many sides are on your die?: "))
  rollDynaDie(userSides)
  again = input("Would you like to roll again? (Y/N): ")
  if again == "N" or again == "n":
    break
  else:
    continue
  
exit()
