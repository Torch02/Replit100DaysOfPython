def colorChange(color, text):
  if color == "red":
    print("\033[0;31m", text, sep="", end="")
  elif color == "pink":
    print("\033[0;35m", text, sep="", end="")
  elif color == "cyan":
    print("\033[0;36m", text, sep="", end="")
  print("\033[0m", sep="", end="")

print("Super Subroutine\n")
print("With my ", end="")
colorChange("pink","new program")
print(" I can just call red(\"and\") ",end="")
colorChange("red", "and")
print(" that word will appear in the color I set it to.\n")
print("With no ", end="")
colorChange("cyan","weird gaps")
print(".\n\nEpic.", end="", sep="")
exit()
