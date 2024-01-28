import os, time
listOfFood = []

def prettyPrint():
  os.system("clear") 
  print("listofFood") 
  print()
  counter = 0
  for order in listOfFood: 
    print(f"{counter}: {order}") 
    counter += 1 
  time.sleep(1)

def printSpam():
  os.system("clear")
  
  for i in range(len(listOfFood)):
    if i < 10:
      os.system("clear")
      print(f"Dear {listOfFood[i]}")
      print("It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.")
      print()
      print("Love and hugs,")
      print("Ian Spammington III")
    else:
      break
    time.sleep(2)
  
while True:
  print("Yummy Food Restaurant")
  menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
  if menu == "1":
    order = input("order > ")
    listOfFood.append(order)
  elif menu =="2":
    order = input ("delete order> ")
    if order in listOfFood:
      listOfFood.remove(order)
  elif menu == "3": 
    prettyPrint()
  elif menu == "4":
    printSpam()
  time.sleep(1)
  os.system("clear")

exit()
