from replit import db
import os, time, random

def addUser():
  tempUser = input("Username: ")
  tempPassword = input("Password: ")
  tempSalt = random.randint(0,99999)
  hashedPassword = hash(f"{tempPassword}{tempSalt}")
  db[tempUser] = {"password":hashedPassword, "salt":tempSalt}
  print(f"User {tempUser} created.")

def login():
  tempUser = input("Username: ")
  tempPassword = input("Password: ")
  try:
    enteredHashedPassword = hash(f"{tempPassword}{db[tempUser]['salt']}")
    if enteredHashedPassword == db[tempUser]['password']:
      print("Login successful")
    else:
      print("Bad username or password")
  except:
    print("Bad username or password")

while True:
  time.sleep(1)
  os.system("clear")
  print("🌟Login System🌟")

  menu = input("1: Add user, 2: Login > ")
  if menu == "1":
    addUser()
  elif menu == "2":
    login()
  else:
    break

exit()
