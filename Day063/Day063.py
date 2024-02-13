import pal 

print("🌟Palindrome Checker🌟")

prompt = input("Input a word > ").lower()

result = pal.isPalindrome(prompt)

if result:
  print(f"{prompt} is a palindrome!")
else:
  print(f"{prompt} is not a palindrome!")

exit()
