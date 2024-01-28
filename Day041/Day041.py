myDictionary = {"name" : "", "url": "", "description": "", "starRating":0}

print("🌟Website Rating🌟")
for tempKey in myDictionary.keys():
  myDictionary[tempKey] = input(f"Input the site {tempKey}: ")
print()
for tempKey, tempValue in myDictionary.items():
  print(f"{tempKey}: {tempValue}\n")

exit()
