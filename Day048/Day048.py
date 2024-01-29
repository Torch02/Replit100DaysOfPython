import os, time
f = open("high.score", "a+")

while True:
  os.system("clear")
  initials = input("Player initials: ")
  score = int(input("Score: "))

  f.write(f"{initials} {score}\n")

  choice = input("Input more scores? (y/n): ")
  if choice.lower()[0] == "y":
    time.sleep(1)
    continue
  else:
    break

f.close()

exit()
