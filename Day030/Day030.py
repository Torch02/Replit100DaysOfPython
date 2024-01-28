print("30 Days Down")
print()

for day in range(1,31):
  tempResponse = input(f"Day {day}:\n")
  tempReply = f"You thought Day {day} was {tempResponse}"
  print(f"{tempReply:^35}")
  

#print("Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame.".format(food=food, location=location, color=color, friend=friend))


exit()
