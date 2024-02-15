class character():
  name = None
  health = None
  mana = None

  def __init__(self, name, health, mana):
    self.name = name
    self.health = health
    self.mana = mana

  def getStatus(self):
    print(f"{self.name} has {self.health} health and {self.mana} magic.")

class player(character):
  lives = None

  def __init__(self, name, health, mana):
    self.name = name
    self.health = health
    self.mana = mana
    self.lives = 3

  def isAlive(self):
    if self.lives > 0:
      print("Yes", end="")
    else:
      print("No", end="")

  def getStatus(self):
    print("Player")
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Magic Points: {self.mana}")
    print(f"Lives: {self.lives}")
    print(f"Alive?: {self.isAlive()}\n")

class enemy(character):
  type = None
  strength = None

  def __init__(self, name, health, mana, type, strength):
    self.name = name
    self.health = health
    self.mana = mana
    self.type = type
    self.strength = strength

class orc(enemy):
  speed = None

  def __init__(self, name, health, mana, strength, speed):
    self.name = name
    self.health = health
    self.mana = mana
    self.type = "Orc"
    self.strength = strength
    self.speed = speed
  
  def getStatus(self):
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Magic Points: {self.mana}")
    print(f"Type: {self.type}")
    print(f"Strength: {self.strength}")
    print(f"Speed: {self.speed}\n")

class vampire(enemy):
  day = None

  def __init__(self, name, health, mana, strength, day):
    self.name = name
    self.health = health
    self.mana = mana
    self.type = "Vampire"
    self.strength = strength
    self.day = day

  def getStatus(self):
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Magic Points: {self.mana}")
    print(f"Type: {self.type}")
    print(f"Strength: {self.strength}")
    print(f"Day/Night: {self.day}\n")

player1 = player("Steve",100,100)

vamp1 = vampire("Roy",100,75,75,"Day")
vamp2 = vampire("Jim",90,60,75,"Day")

orc1 = orc("Billy",50,5,100,60)
orc2 = orc("Fred",60,0,100,75)
orc3 = orc("Jane",45,15,90,80)

print("🌟Generic RPG🌟\n")
player1.getStatus()
vamp1.getStatus()
vamp2.getStatus()
orc1.getStatus()
orc2.getStatus()
orc3.getStatus()

exit()