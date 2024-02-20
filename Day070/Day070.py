import os

userName = input("Username > ")
userPass = input("Password > ")

try:
  if userPass == os.environ[userName]:
    print(f"Welcome, {userName}")
  else:
    print("Bad username or password")
except:
  print("Bad username or password")

exit()
