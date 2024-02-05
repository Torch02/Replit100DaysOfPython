
import os, time, random

myToDo = []

fileExists = True

try:
  f = open("myTasks.txt", "r")
  myToDo = eval(f.read())
  f.close()
except:
  fileExists = False


def autoSave():
  f = open("myTasks.txt", "w")
  f.write(str(myToDo))
  f.close()

def addTask():
  tempRow = []
  tempRow.append(input("What is the task? > ").strip().capitalize())
  tempRow.append(input("When is it due by? > ").strip().capitalize())
  tempRow.append(input("What is the priority? > ").strip().capitalize())

  myToDo.append(tempRow)
  print("Thanks, this task has been added.")    
  print()

def viewTasks():
  option = input("View all tasks or tasks by priority? > ").strip().capitalize()
  if option[0] == "a":
    for row in myToDo:
      print(row)
  else:
    priority = input("What priority of tasks? > ").strip().lower()
    for row in myToDo:
      if priority in row:
        print(row)

def editRow(row):
  tempEdit = input("Do you want to edit the task, due date, or priority? > ").strip().lower()

  if tempEdit[0] == "t":
    newTask = input("What is the new task? > ").strip().capitalize()
    row[0] = newTask
  elif tempEdit[0] == "d":
    newTask = input("What is the new due date? > ").strip().capitalize()
    row[1] = newTask
  elif tempEdit[0] == "p":
    newTask = input("What is the new priority? > ").strip().capitalize()
    row[2] = newTask

def editTask():

  tempTask = input("What task do you want to edit? > ").strip().capitalize()

  for row in myToDo:
    if tempTask in row:
      editRow(row)
      break
    else:
      print(f"The task '{tempTask}' not found.")

  print("Thanks, this task has been edited.")  
  print()

def removeTask():
  tempTask = input("What task do you want to remove? > ").strip().capitalize()

  for row in myToDo:
    if tempTask in row:
      myToDo.remove(row)
      break
    else:
      print(f"The task '{tempTask}' not found.")

  print("Thanks, this task has been edited.")  
  print()

while True:
  os.system("clear")
  print("Life Organizer")
  print()
  task = input("Welcome to the life organizer. Do you want to add, view, edit or remove a to do? > ").strip().lower()

  if task == "add":

    addTask()
    quit = input("Do you want to see the menu again or quit? > ").strip().lower()
    if quit == "quit":
      break
    else:
      continue
      time.sleep(2)

  elif task == "view":

    viewTasks()
    print()

    quit = input("Do you want to see the menu again or quit? > ").strip().lower()
    if quit == "quit":
      break
    else:
      continue
      time.sleep(2)

  elif task == "edit":

    editTask()
    print()

    quit = input("Do you want to see the menu again or quit? > ").strip().lower()
    if quit == "quit":
      break
    else:
      continue
      time.sleep(2)

  elif task == "remove":

    removeTask()
    print()
    quit = input("Do you want to see the menu again or quit? > ").strip().lower()
    if quit == "quit":
      break
    else:
      continue
      time.sleep(2)

  else:
    print("I don't understand that command")
    time.sleep(2)
    continue

  if fileExists:
    try:
      os.mkdir("backup")
    except:
      pass

  backupName = f"backup{random.randint(1,100000000000000000)}.txt"
  os.popen(f"cp myTasks.txt backup/{backupName}")
  autoSave()

exit()