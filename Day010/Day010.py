myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
tip = float(input("What percentage to tip?: "))
perPerson = answer * (round((tip/100), 2) + 1)
print("You all owe", perPerson)
