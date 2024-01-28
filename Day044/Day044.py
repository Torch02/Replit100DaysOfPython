import random, os, time

def createCard():
  rawList = []
  for counter in range(8):
    rawList.append(random.randint(1,90))
  
  rawList.sort()
  
  return [ [rawList[0],rawList[1],rawList[2]],
          [rawList[3],"BINGO",rawList[4]],
          [rawList[5],rawList[6],rawList[7]] ]

def myPrint(card):
  for row in card:
    for item in row:
      print(row, end="\t|\t")

myCard = createCard()
totalXs = 0
active = True
print("Bingo Card Generator")
while active == True:
  
  os.system("clear")
  myPrint(myCard)
  curNumber = int(input("Next number?: "))

  for row in myCard:
    if curNumber in row:
      tempPlace = row.index(curNumber)
      row[tempPlace] = "X"
      print("That was on your card!")
      totalXs += 1
      if totalXs >= 5:
        print("You have won!")
        active = False
        break
      else:
        continue
    time.sleep(2)

exit()
