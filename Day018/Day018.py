secretNumber = 256256
attempts = 0

while True:
  attempts += 1
  currentGuess = int(input("What is my secret number (between 0-1,000,000)? > "))

  if currentGuess < 0:
    print("Your guess is out of bounds. Exiting...")
    exit()
    
  if currentGuess < secretNumber:
    print("You are too low. Guess again")
  elif currentGuess > secretNumber:
    print("You are too high. Guess again")
  elif currentGuess == secretNumber:
    print("Amazing! That's correct. It took you ", attempts, " guess(es)")
    break
exit()
