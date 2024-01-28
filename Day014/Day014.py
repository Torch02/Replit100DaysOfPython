from getpass import getpass as input

print("Rock Paper Scissors!")
print("")
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
  elif player_2 == "S" or player_2 == "s":
    print("Player 1 wins, rock over scissors!")
  else:
    print("No cheating, Player 2! Bad input.")
elif player_1 == "P" or player_1 == "p":
  if player_2 == "R" or player_2 == "r":
    print("Player 1 wins, paper over rock!")
  elif player_2 == "P" or player_2 == "p":
    print("It's a tie! Both players chose paper")
  elif player_2 == "S" or player_2 == "s":
    print("Player 2 wins, scissors cut paper!")
  else:
    print("No cheating, Player 2! Bad input.")
elif player_1 == "S" or player_1 == "s":
  if player_2 == "R" or player_2 == "r":
    print("Player 2 wins, rock over scissors!")
  elif player_2 == "P" or player_2 == "p":
    print("Player 1 wins, scissors cut paper!")
  elif player_2 == "S" or player_2 == "s":
    print("It's a tie! Both players chose scissors!")
  else:
    print("No cheating, Player 2! Bad input.")
else:
  print("No cheating, Player 1! Bad input.")
