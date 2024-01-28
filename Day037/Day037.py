firstName = input("What is your first name?: ")
lastName = input("What is your last name?: ")
maidenName = input("What is your mother's maiden name?: ")
cityName = input("What is your birth city?: ")


starName = f"{firstName.strip().lower().capitalize()[0:3]}{lastName.strip().lower()[0:3]} {maidenName.strip().lower().capitalize()[0:2]}{cityName.strip().lower()[len(cityName)-3:]}"

print(f"\nYour Star Wars name is {starName}")

exit()
