import csv # Imports the csv library

with open("Day54Totals.csv") as file: 
  reader = csv.DictReader(file) # Treats the file as a dictionary 
  total = 0.0
  for row in reader: 
    total += float(row["Cost"])*float(row["Quantity"])

print("🌟Shop $$ Tracker🌟")
print(f"Your shop took in ${round(total,2)} total.")

exit()
