import random#,os, time

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

wordChosen = random.choice(listOfWords)
answerState = ""
lettersGuessed = []

for i in range(0,len(wordChosen)):
  answerState += "_"

livesRemaining = 6

def getProgress():
  answerState = ""
  for i in wordChosen:
    if i in lettersGuessed:
      answerState = answerState + i
    else:
      answerState = answerState + "_"
  return answerState

print("🌟Hangman🌟\n")

while livesRemaining >= 0:
  currentLetter = input("Choose a letter: ").lower()

  if currentLetter in lettersGuessed:
    print(f"You've already guessed {currentLetter}\n")
    continue
  else:
    lettersGuessed.append(currentLetter)
    if currentLetter in wordChosen:
      #
      answerState = getProgress()
      #
      print("Correct")
      print(f"{answerState}\n")

      if "_" in answerState:
        continue
      else:
        print("You've won!")
        break
    else:
      livesRemaining -= 1
      print("Nope, not in there")
      print(f"{livesRemaining} lives left.\n")

if livesRemaining < 0:
  print(f"Sorry, the correct answer was {wordChosen}")

exit()
