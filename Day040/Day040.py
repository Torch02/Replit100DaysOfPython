print("🌟Contact Card🌟")
myUser = {}

myUser['name'] = input("Input your name: ")
myUser['dob'] = input("Input your date of birth: ")
myUser['phone'] = input("Input your telephone number: ")
myUser['email'] = input("Input your email: ")
myUser['address'] = input("Input your address: ")

print()
print(f"Hello {myUser['name']}. Our records show that you were born on {myUser['dob']}, we can call you on {myUser['phone']}, e-mail you at {myUser['email']}, or post you at {myUser['address']}")

exit()
