import os

mokedex = {}
def prettyPrint():
  print()

  for key, value in mokedex.items():

    print(key, end=": ")
    for subKey, subValue in value.items():
      print(f"{subKey}: {subValue}", end=" | ")
    print()

while True:
  
  os.system("clear")
  print("Mokebeast Generator\n")
  
  name = input("Name: ")
  type = input("Type: ")
  move = input("Special move: ")
  hp   = input("HP: ")
  mp   = input("MP: ")

  mokedex[name] = {"Type": type, "Special move":move, "HP":hp, "MP":mp} 


  again = input("Another? Yes/No > ")
  if again[0].lower() == "y":
    continue
  else:
    break

prettyPrint()

exit()
