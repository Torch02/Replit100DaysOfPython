print("Auto Grade Book")
print("")
name = input("What test did you take? ")
print("")
totalPoints = int(input("How many total points were there? "))
print("")
score = int(input("How many points did you earn? "))

percent = 100 * round(float(score / totalPoints), 2)

if percent >= 90:
  letter = "an A+"
elif percent < 90 and percent >= 80:
  letter = "an A"
elif percent < 80 and percent >= 70:
  letter = "a B"
elif percent < 70 and percent >= 60:
  letter = "a C"
elif percent < 60 and percent >= 50:
  letter = "a D"
else: 
  letter = "Dude, WTF?!?!"

print("")
print("On your ", name, " test you scored ", percent, "%, which is - ", letter)
