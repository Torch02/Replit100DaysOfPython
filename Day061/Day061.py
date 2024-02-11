from replit import db
import os, time, datetime

while True:
  time.sleep(1)
  os.system("clear")

  menu = int(input("1. Add tweet, 2. View tweets > "))

  if menu == 1:
    tempNewTweet = input("What do you want to tweet? > ")
    tempTimeStamp = datetime.datetime.now()
    db[f"mes{tempTimeStamp}"] = tempNewTweet
    continue    
  elif menu == 2:
    allKeys = db.prefix("mes")
    allKeys = allKeys[::-1]
    for key in allKeys:
      print(f"{key}: {db[key]}")
    time.sleep(5)
  else:
    print("That's not an option.")
    break

exit()
