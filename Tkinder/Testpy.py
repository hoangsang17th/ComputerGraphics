# from tkinter import *
# import math

# #defining main function
# def main():

# #main starts
# #reading end points of line
# x0 = int(input("ENTER THE Xo : "))
# y0 = int(raw_input("ENTER THE Yo : "))
# x1 = int(raw_input("ENTER THE Xn : "))
# y1 = int(raw_input("ENTER THE Yn : "))
# root = Tk()
# pic = PhotoImage(width=800,height=800)
# lb = Label(root,image=pic)
# lb.pack()
# color = "blue"

# #Now Drawing Line

# steep = abs(y1 - y0) > abs(x1 - x0)
# if steep:
# x0, y0 = y0, x0
# x1, y1 = y1, x1 #if ends
# if x0 > x1:
# x0, x1 = x1, x0
# y0, y1 = y1, y0
# if y0 < y1:
# ystep = 1
# else:
# ystep = -1

# deltax = x1 - x0
# deltay = abs(y1 - y0)
# error = -deltax / 2
# y = y0
# for x in range(x0, x1 + 1):
# if steep:
# pic.put(color,(y,x)) #if end
# else:
# pic.put(color,(x,y)) #else end

# error = error + deltay
# if error > 0:
# y = y + ystep
# error = error - deltax #if end
# root.mainloop() #main ends

# main()