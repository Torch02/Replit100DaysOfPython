import os, random, time

cardDeck = {}

cardDeck["Patrick Mahomes"] = {"Speed":84,"Strength":70,"Agility":81,"Awareness":99}
cardDeck["Lamar Jackson"] = {"Speed":96,"Strength":63,"Agility":95,"Awareness":98}
cardDeck["Brock Purdy"] = {"Speed":78,"Strength":63,"Agility":81,"Awareness":88}
cardDeck["Jared Goff"] = {"Speed":76,"Strength":64,"Agility":74,"Awareness":81}

p1Deck = {}
p2Deck = {}

def dealCards():
  cardList = list(cardDeck.keys())
  card1 = random.choice(cardList)
  p1Deck[card1] = cardDeck[card1]
  cardList.remove(card1)
  card2 = random.choice(cardList)
  p1Deck[card2] = cardDeck[card2]
  cardList.remove(card2)

  # assumes there are only two players, so remaining cards to p2
  for card in cardList:
    p2Deck[card] = cardDeck[card]

dealCards()

while True:
  os.system("clear")
  print("🌟Top Trumps🌟\n")
  print("Welcome to Top Trumps 'Conference Championship Maden QB Ratings' Simulator\n")

  print(f"1 - {list(p1Deck.keys())[0]}")
  print(f"2 - {list(p1Deck.keys())[1]}")
  
  p1CardChoice = int(input("> ")) - 1
  p1CardName = list(p1Deck.keys())[p1CardChoice]
  p1StatChoice = int(input("Choose your stat:\n1. Speed\n2. Strength\n3. Agility\n4. Awareness\n\n> "))

  if p1StatChoice == 1:
    statName = "Speed"
  elif p1StatChoice == 2:
    statName = "Strength"
  elif p1StatChoice == 3:
    statName = "Agility"
  else:
    statName = "Awareness"

  p2CardName = random.choice(list(p2Deck.keys()))

  print(f"{p1CardName} has a {statName} stat of {p1Deck[p1CardName][statName]}")
  print(f"{p2CardName} has a {statName} stat of {p2Deck[p2CardName][statName]}")

  if p1Deck[p1CardName][statName] > p2Deck[p2CardName][statName]:
    print(f"*** {p1CardName} is the winner ***\n")
  else:
    print(f"*** {p2CardName} is the winner ***\n")

  repeat = input("Again? y/n > ")

  if repeat.lower()[0] == "y":
    time.sleep(2)
    continue
  else:
    break
  

exit()
