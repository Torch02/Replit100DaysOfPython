myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  tempFirstName = input("First Name > ").strip().lower().capitalize()
  tempLastName = input("Last Name > ").strip().lower().capitalize()

  addItem = f"{tempFirstName} {tempLastName}"
  
  if addItem not in myList:
    myList.append(addItem)
    printList()
  else:
    print(f"{addItem} is already in the list\n")

  moreNames = input("Add another name? (y/n)?: ").strip().lower()
  if moreNames == "y":
    continue
  else:
    break

exit()
