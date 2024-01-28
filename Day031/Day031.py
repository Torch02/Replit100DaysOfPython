def colorChange(color, text):
  if color == "red":
    print("\033[0;31m", text, sep="", end="")
  elif color == "pink":
    print("\033[0;35m", text, sep="", end="")
  elif color == "blue":
    print("\033[0;34m", text, sep="", end="")
  elif color == "yellow":
    print("\033[1;33m", text, sep="", end="")
  elif color == "green":
    print("\033[0;32m", text, sep="", end="")
  print("\033[0m", sep="", end="")

# Interface 1
colorChange("red", "=")
print("=", end="", sep="")
colorChange("blue", "=")
print(" Music App ", end="", sep="")
colorChange("blue", "=")
print("=", end="", sep="")
colorChange("red", "=")
print()

print("🔥▶️\tRadio Gaga")
print("\t", sep="", end="")
colorChange("yellow","Queen")
print("\n\n")

print("PREV")
print("\t", sep="", end="")
colorChange("green"," NEXT")
print("\n", sep="", end="")
print("\t\t", sep="", end="")
colorChange("pink","  PAUSE")
print()
print()
print()


# Interface 2
welcome = "WELCOME TO"
print(f"{welcome: ^35}")
print("\033[0;34m", sep="", end="")
armbook = "--\tARMBOOK\t--"
print(f"{armbook: ^35}")
print("\033[1;33m", sep="", end="")
yellow1 = "Definitely not a rip off of"
print(f"{yellow1: >35}")
yellow2 = "a certain other social"
print(f"{yellow2: >35}")
yellow3 = "networking site."
print(f"{yellow3: >35}")
print()
print()

print("\033[0;31m", sep="", end="")
honest = "Honest."
print(f"{honest: ^35}")
print()
print("\033[1;37m", sep="", end="")
username = "Username:"
print(f"{username: ^35}")
password = "Password:"
print(f"{password: ^35}")


exit()
