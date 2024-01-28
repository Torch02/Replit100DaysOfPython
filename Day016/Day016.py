print("Fill in the blank lyrics!")
print("(Type in the blank lyrics and see if you are as cool as me.)")
guesses = 1
while True:
  lyric = input("Never going to ______ you up. ")
  if lyric == "give":
    break
  else:
    print("Nope, try again.")
    guesses += 1
print("Well done! It only took you ", guesses, " attempts")
