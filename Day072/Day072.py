from replit import db
import os, time, random, datetime

successfulAuth = False

def addUser():
  tempUser = input("Username: ")
  tempPassword = input("Password: ")
  tempSalt = random.randint(0,99999)
  hashedPassword = hash(f"{tempPassword}{tempSalt}")
  db[tempUser] = {"password":hashedPassword, "salt":tempSalt}
  print(f"User {tempUser} created.")

def login():
  global successfulAuth
  tempUser = input("Username: ")
  tempPassword = input("Password: ")
  try:
    enteredHashedPassword = hash(f"{tempPassword}{db[tempUser]['salt']}")
    if enteredHashedPassword == db[tempUser]['password']:
      print("Login successful")
      successfulAuth = True
    else:
      print("Bad username or password")
  except:
    print("Bad username or password")

keys = db.keys()
keycount = len(keys)

while not successfulAuth:
  if keycount > 0:
    login()
  else:
    addUser()

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
    time.sleep(2)

  elif menu == 3:
    break

  else:
    print("That's not an option.")
    time.sleep(2)
    continue


exit()