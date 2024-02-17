import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

def changeImage(): # new Subroutine
  global canvas, text, container, hello
  prompt = text.get("1.0","end").lower().strip()
  if prompt == "charlotte":
    canvas.itemconfig(container,image=charlotte)
  elif prompt == "gerald":
    canvas.itemconfig(container,image=gerald)
  elif prompt == "katie":
    canvas.itemconfig(container,image=katie)
  elif prompt == "mo":
    canvas.itemconfig(container,image=mo)
  else:
    hello["text"] = "Unable to find this user"
  
hello = tk.Label(text = "Guess Who?") 
hello.pack() 

text = tk.Text(window ,height=1, width = 50)
text.pack()

button = tk.Button(text = "Find", command=changeImage) # Given the button a command to call the changeImage subroutine.
button.pack()


canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack()

charlotte = ImageTk.PhotoImage(Image.open(".tutorial/Guess Who/charlotte.jpg"))
gerald = ImageTk.PhotoImage(Image.open(".tutorial/Guess Who/gerald.jpg"))
katie = ImageTk.PhotoImage(Image.open(".tutorial/Guess Who/katie.jpg"))
mo = ImageTk.PhotoImage(Image.open(".tutorial/Guess Who/mo.jpg"))

container = canvas.create_image(150,1,image=None) # Assigned create image to the container variable


tk.mainloop()

exit()