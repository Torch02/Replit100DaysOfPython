print("The times tables!")
print()
base = int(input("Name your multiples: "))
score = 0

for i in range(1,11,1):
  curAnswer = i * base
  curQuestion = str(i) + " X " + str(base) + " = "
  str()
  curGuess = int(input(curQuestion))
  if curGuess == curAnswer:
    score += 1
    print("Correct!")
  else:
    print("Incorrect. The answer is ", curAnswer)

print("---")
print("You scored ", score, " out of 10.")
exit()
