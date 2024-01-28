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
    myAgenda.append(item)
  elif menu == "edit":
    item = input("What item did you complete?: ")
    if item in myAgenda:
      myAgenda.remove(item)
    else:
      print(f"{item} is not on your agenda")
      time.sleep(1)
      continue
  elif menu == "view":
    printList()
  elif menu == "":
    break
  else:
    print("I don't understand that command")
    time.sleep(3)
    continue

exit()

