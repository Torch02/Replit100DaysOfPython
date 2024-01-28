secondsInAMinute = 60
minutesInAnHour = 60
hoursInADay = 24

leapYear = input("Is this a leap year?: ")
if leapYear == 'yes':
  daysInAYear = 366
else:
  daysInAYear = 365

secondsInAYear = secondsInAMinute * minutesInAnHour * hoursInADay * daysInAYear

print("There are ", secondsInAYear, " seconds in this year")
