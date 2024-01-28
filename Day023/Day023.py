def loginPrompt():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password?: ")
  
    if username == "david" and password == "baldies4life":
      print("Welcome to Replit!")
      break
    else:
      print("Bad username or password")
      continue

loginPrompt()
exit()
