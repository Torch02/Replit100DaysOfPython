import tkinter as tk

window = tk.Tk()
window.title("Calculator") 
window.geometry("300x300") 

answer = 0
lastNumber = 0
operator = None

def updateLabel(input):
  global answer
  answer = f"{answer}{input}" # I don't understand why this part appears necesasry
  answer = int(answer)
  hello["text"] = answer

def command(op):
  global answer, lastNumber, operator
  lastNumber = answer
  answer = 0
  if op == "+":
    operator = "+"
  elif op == "-":
    operator = "-"
  elif op == "*":
    operator = "*"
  elif op == "/":
    operator = "/"
  hello["text"] = answer
  
def calc():
  global answer, lastNumber, operator
  if operator == "+":
    total = lastNumber + answer
  elif operator == "-":
    total = lastNumber + answer
  elif operator == "*":
    total = lastNumber + answer
  elif operator == "/":
    total = lastNumber / answer
  answer = total
  hello["text"] = answer
  
hello = tk.Label(text = answer)
hello.grid(row=0, column=1)

# I wish they would have explained what "lambda" is doing, rather than throwing it in the hints
oneButton = tk.Button(text = "1", command= lambda: updateLabel("1")).grid(row=1, column=0)
twoButton = tk.Button(text = "2", command= lambda: updateLabel("2")).grid(row=1, column=1)
threeButton = tk.Button(text = "3", command= lambda: updateLabel("3")).grid(row=1, column=2)
plusButton = tk.Button(text = "+", command= lambda: command("+")).grid(row=1, column=3)
minusButton = tk.Button(text = "-", command= lambda: command("-")).grid(row=1, column=4)
fourButton = tk.Button(text = "4", command= lambda: updateLabel("4")).grid(row=2, column=0)
fiveButton = tk.Button(text = "5", command= lambda: updateLabel("5")).grid(row=2, column=1)
sixButton = tk.Button(text = "6", command= lambda: updateLabel("6")).grid(row=2, column=2)
timesButton = tk.Button(text = "*", command= lambda: command("*")).grid(row=2, column=3)
divideButton = tk.Button(text = "/", command= lambda: command("/")).grid(row=2, column=4)
sevenButton = tk.Button(text = "7", command= lambda: updateLabel("7")).grid(row=3, column=0)
eightButton = tk.Button(text = "8", command= lambda: updateLabel("8")).grid(row=3, column=1)
nineButton = tk.Button(text = "9", command= lambda: updateLabel("9")).grid(row=3, column=2)
equalsButton = tk.Button(text = "=", command=calc).grid(row=4, column=3)
zeroButton = tk.Button(text = "0", command= lambda: updateLabel("0")).grid(row=4, column=1)

tk.mainloop()

exit()
