amountBorrowed = 1000
rate = 0.05
totalCost = amountBorrowed
years = 10

for i in range(years):
  totalCost = (1 + rate)*totalCost
  print("Year ", i + 1, " is ", round(totalCost, 2))

print("You paid $", round(totalCost - amountBorrowed, 2), " in interest.")
exit()
