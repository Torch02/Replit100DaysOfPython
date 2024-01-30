f = open("high.score", "r")

scores = {}

while True:
  tempLine = f.readline().strip()
  if tempLine == "":
    break
  else:
    scores[tempLine.split()[0]] = int(tempLine.split()[1])

highName = ""
highScore = 0

for name in scores.keys():
  if scores[name] > highScore:
    highName = name
    highScore = scores[name]

print(f"The best player is {highName} with a score of {highScore}")

exit()
