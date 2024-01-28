answer = ""
while answer != "yes":
  animal = input("What animal do you want? ")
  if animal == "dog":
    print("A dog goes woof")
  elif animal == "cat":
    print("A cat goes meow")
  elif animal == "lion":
    print("A lion goes roar")
  else:
    print("A ", animal, "goes awooga!")
  answer = input("Do you want to exit? ")
