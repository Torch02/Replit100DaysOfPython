
from replit import db
import os, time, datetime

correctPassword = "P@$$word1!"

# I should be less lazy and go back to look how secure/masked input was done in the rock/paper/scissors lesson
passwordEntered = input("What is the password? > ")

if passwordEntered != correctPassword:
  print("Wrong password")
  exit()

while True:
  time.sleep(1)
  os.system("clear")

  menu = int(input("1. Add diary entry, 2. View entries, 3. Exit > "))

  if menu == 1:
    tempNewDiary = input("Your entry: ")
    tempTimeStamp = datetime.datetime.now()
    db[f"Diary-{tempTimeStamp}"] = tempNewDiary
    continue    
    
  elif menu == 2:
    moreEntries = True
    entryCount = 0
    allKeys = db.prefix("Diary-")
    allKeys = allKeys[::-1]

    while moreEntries:
      try: 
        print(f"{allKeys[entryCount]}: {db[allKeys[entryCount]]}")
        entryCount += 1
        moreEntryMenu = input("View another entry? y/n > ").lower()
        if moreEntryMenu[0] == "y":
          os.system("clear")
          continue
        else:
          moreEntries = False
      except:
        print("No more entries available")
        moreEntries = False
    time.sleep(3)
    
  elif menu == 3:
    break
    
  else:
    print("That's not an option.")
    time.sleep(2)
    continue

exit()
