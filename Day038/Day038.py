def rainbowize (letter):
  if letter == "b":
    print("\033[0;34m", end="") #blue
  elif letter == "g":
    print("\033[0;32m", end="") #green
  elif letter == "p":
    print("\033[0;35m", end="") #purple
  elif letter == "r":
    print("\033[0;31m", end="") #red
  elif letter == "y":
    print("\033[33m", end="") #yellow
  elif letter == " ":
    print("\033[0m", end="") #back to default

myString = input("What sentence do you want to rainbowize?:\n")

for i in myString:
  rainbowize(i.lower())
  print(i, end="")

exit()
