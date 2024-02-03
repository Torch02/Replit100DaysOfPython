import os, time

inventory = []

def loadInventory(debug):
  try:
    f = open("inventory.txt","r")
    toLoad = eval(f.read())
    f.close()
    return toLoad

  except Exception:
    if debug:
        print("ERROR: Unable to load")
    return []

def saveInventory(toSave):
  try:
    f = open("inventory.txt","w")
    f.write(str(toSave))
    f.close()
  except Exception:
    print("ERROR: Unable to write to inventory.txt")

def addToInventory():
  itemToAdd = input("Input the item to add: > ").lower().capitalize()
  inventory.append(itemToAdd)
  print(f"{itemToAdd} has been added to your inventory.")
  saveInventory(inventory)

def removeFromInventory():
  itemToRemove = input("Input the item to add: > ").lower().capitalize()
  if itemToRemove in inventory:
    inventory.remove(itemToRemove)
    print(f"{itemToRemove} has been removed from your inventory.")
    saveInventory(inventory)
  else:
    print(f"You have no {itemToRemove}s in your inventory")

def viewInventory():
  viewChoice = input("Input the item to view: > ").lower().capitalize()
  tempCount = inventory.count(viewChoice)
  if tempCount == 0:
    print(f"You have no {viewChoice}s in your inventory")
  elif tempCount == 1:
    print(f"You have one {viewChoice}")
  else:
    print(f"You have {tempCount} {viewChoice}s")

inventory = loadInventory(False)

while True:
  os.system("clear")
  print("🌟RPG Inventory🌟\n")

  menu = input("1: Add  2: Remove  3: View  > ")

  if menu == "1":
    addToInventory()
  elif menu == "2":
    removeFromInventory()
  elif menu == "3":
    viewInventory()
  else:
    print("That's not a valid option.")
    time.sleep(2)
    continue

  choice = input("Continue? y/n > ").lower()
  if choice[0] == "y":
    time.sleep(1)
    continue
  else:
    break

exit()