def isPalindrome(word):
  tempLength = len(word)
  if tempLength == 1:
    return True
  elif tempLength == 2:
    if word[0] == word[1]:
      return True
    else:
      return False
  else:
    if word[0] == word[-1]:
      tempSubString = word[1:-1]
      return isPalindrome(tempSubString)
    else:
      return False