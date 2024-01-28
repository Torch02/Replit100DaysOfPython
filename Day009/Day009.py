print("Generation Generator")
print()
year = int(input("What year were you born?: "))
if year < 1925:
  print("You're pretty computer savvy for someone that age!")
elif year >= 1925 and year <= 1946:
  print("You're a Traditionalist!")
elif year >= 1947 and year <= 1964:
  print("Ok, Boomer!")
elif year >= 1965 and year <= 1981:
  print("You're GenX!")
elif year >= 1982 and year <= 1995:
  print("You're a Millenial!")
elif year >= 1996 and year <= 2015:
  print("You're GenZ!")
else:
  print("Aren't you a little young for this??")
