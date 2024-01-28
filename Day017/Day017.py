from getpass import getpass as input

print("Rock Paper Scissors!")
print("")

p1score = 0
p2score = 0

while True:
  print("Select your move (R, P, or S)")
  print("")
  player_1 = input("Player 1 > ")
  print("")
  player_2 = input("Player 2 > ")
  print("")
  
  if player_1 == "R" or player_1 == "r":
    if player_2 == "R" or player_2 == "r":
      print("It's a tie! Both players chose rock")
    elif player_2 == "P" or player_2 == "p":
      print("Player 2 wins, paper over rock!")
      p2score += 1
    elif player_2 == "S" or player_2 == "s":
      print("Player 1 wins, rock over scissors!")
      p1score += 1
    else:
      print("No cheating, Player 2! Bad input.")
      continue
  elif player_1 == "P" or player_1 == "p":
    if player_2 == "R" or player_2 == "r":
      print("Player 1 wins, paper over rock!")
      p1score += 1
    elif player_2 == "P" or player_2 == "p":
      print("It's a tie! Both players chose paper")
    elif player_2 == "S" or player_2 == "s":
      print("Player 2 wins, scissors cut paper!")
      p2score += 1
    else:
      print("No cheating, Player 2! Bad input.")
      continue
  elif player_1 == "S" or player_1 == "s":
    if player_2 == "R" or player_2 == "r":
      print("Player 2 wins, rock over scissors!")
      p2score += 1
    elif player_2 == "P" or player_2 == "p":
      print("Player 1 wins, scissors cut paper!")
      p1score += 1
    elif player_2 == "S" or player_2 == "s":
      print("It's a tie! Both players chose scissors!")
    else:
      print("No cheating, Player 2! Bad input.")
      continue
  else:
    print("No cheating, Player 1! Bad input.")
    continue
  if p1score == 3:
    print("Congrats Player 1 on winning ", p1score, " to ", p2score)
    break
  elif p2score == 3:
    print("Congrats Player 2 on winning ", p2score, " to ", p1score)
    break
  else:
    continue
