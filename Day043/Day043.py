import random

print("Bingo Card Generator")

rawList = []
for counter in range(8):
  rawList.append(random.randint(1,90))

rawList.sort()

card = [ [rawList[0],rawList[1],rawList[2]],
        [rawList[3],"BINGO",rawList[4]],
        [rawList[5],rawList[6],rawList[7]] ]

def myPrint():
  for row in card:
    print(row)

myPrint()

exit()
