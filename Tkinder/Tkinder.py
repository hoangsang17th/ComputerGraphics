from tkinter import * 
from tkinter.ttk import *

root = Tk()
root.title("Bresenham Algorithm")
style = Style()

style.configure('W.TButton', font =('calibri', 13, 'bold', 'underline'), width=20)
# myLabel1 = Label(root, text=" Hello World")
# myLabel2 = Label(root, text=" I'm Pham Hoang Sang")
myCanvas = Canvas(root)
myCanvas.pack()

def create_circle(x =100, y=100, r=50): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return myCanvas.create_oval(x0, y0, x1, y1)


myButton = Button(root, text="Click Me!",style = 'W.TButton',command=create_circle)
# myLabel1.pack()
# myLabel2.pack()
# myLabel1.grid(row=0, column = 0)
# myLabel2.grid(row=0, column = 5)
myButton.pack()


root.mainloop()

# from tkinter import *
# root = Tk()
# myCanvas = Canvas(root)
# myCanvas.pack()

# def create_circle(x, y, r, canvasName): #center coordinates, radius
#     x0 = x - r
#     y0 = y - r
#     x1 = x + r
#     y1 = y + r
#     return canvasName.create_oval(x0, y0, x1, y1)

# create_circle(100, 100, 20, myCanvas)
# create_circle(50, 25, 10, myCanvas)
# root.mainloop()