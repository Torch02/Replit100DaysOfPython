import os, time

pizzaOrders = []

def loadOrders():
  try:
    f = open("pizza.orders","r")
    toLoad = eval(f.read())
    f.close()
    return toLoad

  except Exception:
    print("ERROR: Unable to load")
    return []

def saveOrders(toSave):
  try:
    f = open("pizza.orders","w")
    f.write(str(toSave))
    f.close()
  except Exception:
    print("Error writing to pizza.orders")

pizzaOrders = loadOrders()

while True:
  os.system("clear")
  print("🌟Dave's Dodgy Pizzas🌟\n")

  try:
    tempQty = int(input("How many pizzas? > "))

  except Exception:
    tempQty = int(input("Quantity must be a numerical character, try again > "))

  tempSize = input("What size pie? > ")
  tempName = input("Your name? > ")
  tempPrice = tempQty * len(tempSize)

  pizzaOrders.append([tempName, tempSize, tempQty, tempPrice])
  print(f"Thanks {tempName}, you pizzas will cost ${tempPrice}")

  saveOrders(pizzaOrders)

  choice = input("Another order? y/n > ").lower()
  if choice[0] == "y":
    time.sleep(1)
    continue
  else:
    break

exit()
