def factorial(number):
  if number == 1:
    return 1
  else:
    return number * factorial(number - 1)

print("🌟Factorial Finder🌟")
number = int(input("Input a number > "))
fac = factorial(number)
print(f"The factorial of {number} is {fac}.")

exit()
