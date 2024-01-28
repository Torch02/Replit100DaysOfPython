import random

print("Totally Random 1,000,000 to 1")

myNumber = random.randint(1, 1000000)

while True:
  curGuess = int(input("What is your guess?: "))
  if curGuess == myNumber:
    print("Correct!!")
    break
  elif curGuess < myNumber:
    print("Too low")
    continue
  else:
    print("Too High")
    continue

exit()
