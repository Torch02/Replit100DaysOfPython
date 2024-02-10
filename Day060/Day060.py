import datetime

today = datetime.date.today() 

print("🌟Event Countdown Timer🌟")

name = input("Input the event > ")
year = int(input("Input the year > "))
month = int(input("Input the month > "))
day = int(input("Input the day > "))
holiday = datetime.date(year = year, month = month, day = day) 
delta = abs((holiday - today).days)

if today < holiday:
  print(f"{name} is in {delta} days")
elif today > holiday:
  print(f"{name} was {delta} days ago")
else:
  print(f"{name} is today!!")

exit()