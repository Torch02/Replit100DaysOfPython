import os, time, random

while True:
  os.system("clear")
  print("🌟Idea Storage🌟\n")
  addOrView = input("Add an idea or see a random idea? (a/r) > ").strip().lower()

  if addOrView[0] == "a":
    tempIdea = input("Input your idea > ")
    f = open("my.ideas","a+")
    f.write(f"{tempIdea}\n")
    f.close()
    print("Your idea has been stored.")
  elif addOrView[0] == "r":
    
    f = open("my.ideas","r")
    allIdeas = f.read().split("\n")
    f.close()
    allIdeas.remove("")
        
    if len(allIdeas) == 0:
      print("There were no ideas stored!")
    else:
      randomIdea = random.choice(allIdeas)
      print(randomIdea)
  else:
    print("I don't understand that command")

  again = input("Continue or exit? > ").strip().lower()
  if again[0] == "c":
    time.sleep(1)
    continue
  else:
    break
  

exit()
