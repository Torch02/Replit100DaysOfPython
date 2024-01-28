print("Counting By!")
print()
start = int(input("Where would you like to start?: "))
end = int(input("Where do you want to end before?: "))
incr = int(input("How many should we count by?: "))

for i in range(start, end, incr):
  print(i)
