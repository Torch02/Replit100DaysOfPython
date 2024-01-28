print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
mokeBeastDetails = {}

def colorize (color):
  if color == "blue":
    print("\033[0;34m", end="") #blue
  elif color == "brown":
    print("\033[0;33m", end="") #brown
  elif color == "red":
    print("\033[0;31m", end="") #red
  elif color == "yellow":
    print("\033[33m", end="") #yellow
  elif color == " ":
    print("\033[0m", end="") #back to default

mokeBeastDetails["name"] = input("What is your beast's name?: ").strip().capitalize()
mokeBeastDetails["type"] = input("What is your beast's type?\n(earth, fire, air, water or spirit): ").strip()
mokeBeastDetails["move"] = input("What is your beast's special move?: ").strip().capitalize()
mokeBeastDetails["hp"] = input("What is your beast's starting HP?: ").strip().capitalize()
mokeBeastDetails["mp"] = input("What is your beast's starting MP?: ").strip().capitalize()

article = "a"

if mokeBeastDetails["type"] == "earth":
  colorize("brown")
  article = "an"
elif mokeBeastDetails["type"] == "fire":
  colorize("red")
elif mokeBeastDetails["type"] == "air":
  colorize(" ")
  article = "an"
elif mokeBeastDetails["type"] == "water":
  colorize("blue")
elif mokeBeastDetails["type"] == "spirit":
  colorize("yellow")
  

print(f"Your MokeBeast is called {mokeBeastDetails['name']}. It is {article} {mokeBeastDetails['type']} beast with a special move {mokeBeastDetails['move']}")

exit()

