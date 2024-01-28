from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    anyButton = input("Press Spacebar, then Enter, to pause & return to menu")
    if anyButton == " ":
      source.paused = True
      return
    else:
      continue


while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  print("🎵 MyPOD Music Player")
  print("Press 1 to Play")
  print("Press 2 to Exit")
  print("Press anything else to see the menu again.")
  # take user's input
  menuInput = input()
  # check whether you should call the play() subroutine depending on user's input
  if menuInput == "1":
    play()
  elif menuInput == "2":
    break
  else:
    continue

exit()
