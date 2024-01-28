import os, time

myAgenda = []

def printList():
  time.sleep(1)
  os.system("clear")
  print() #this is just to add an extra space between items
  for i in myAgenda:
    print(i)
  print() #this is just to add an extra space between items

menu = ""

while True:
  time.sleep(1)
  if menu == "view":
    print()
  else:
    os.system("clear")
    
  print("To Do List Manager")
  menu = input("Do you want to view, add, or edit your list: \n")
  if menu == "add":
    item = input("What's next on the agenda?: ")
    if item in myAgenda:
      print(f"{item} is already in the list!")
      continue
    else:
      myAgenda.append(item)
  elif menu == "edit":
    submenu = input("Do you want to remove an item, edit an item, or delete the list?: ")
    if submenu == "remove":
      subitem = input("What item shall we remove?: ")
      if item in myAgenda:
        confirm = input(f"Are you sure you want to remove {subitem}? (y/n): ")
        if confirm == "y":
          myAgenda.remove(item)
        else:
          print("Ok. Glad I double checked")
          continue
      else:
        print(f"{item} is not on your agenda")
        time.sleep(1)
        continue
    elif submenu == "edit":
      subitem = input("What shall we edit?: ")
      if subitem in myAgenda:
        myAgenda.remove(subitem)
        newitem = input("What is the new version?: ")
        myAgenda.add(newitem)
      else:
        print(f"{subitem} is not on your agenda")
        continue
    elif submenu == "delete":
      myAgenda = []  
  elif menu == "view":
    printList()
  elif menu == "":
    break
  else:
    print("I don't understand that command")
    time.sleep(3)
    continue

exit()

