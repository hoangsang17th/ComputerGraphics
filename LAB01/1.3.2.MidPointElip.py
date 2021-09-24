# Đã XONG
import matplotlib.pyplot as plt
import numpy
import math
from matplotlib.backend_bases import MouseButton

plt.title("Bresenham Algorithm- Elip")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.imshow(numpy.zeros((500, 500)), "Blues")

def bres(xc, yc, a , b):
    
    a2 = a * a
    b2 = b * b
    x = 0
    y = b
    # Giá trị p tại điểm dầu tiên (0, r) có giá trị
    p =  b2-a2 *b  + (1/4)*a2
    x0 = int(a2/(math.sqrt(a2+b2)))
    y0 = int(b2/(math.sqrt(a2+b2)))
    data = numpy.zeros((500, 500))
    while x < x0:
        # Hàm này cố định cho hình Elip
        data[x+xc, y+yc]=1
        data[x+xc, -y+yc]=1
        data[-x+xc, -y+yc]=1
        data[-x+xc, y+yc]=1
        
        if p < 0:
            p = p + b2*(2*x+3)
        else: 
            p = p + (2*x+3)*b2-2*a2*(y-1)
            y = y - 1
            
        x = x + 1
    
    x = a 
    y = 0
    p = a2-a*b2 +(1/4)*b2
    while y < y0:
        # Hàm này cố định cho hình Elip
        data[x+xc, y+yc]=1
        data[x+xc, -y+yc]=1
        data[-x+xc, -y+yc]=1
        data[-x+xc, y+yc]=1
        
        if p < 0:
            p = p + a2*(2*y+3)
        else: 
            p = p + a2*(2*y+3)- 2*b2*(x-1)
            x = x - 1
            
        y = y + 1
        
    
    plt.imshow(data, "Blues")
    plt.draw()
            

    
    

xc =250
yc =250
a =0
b =0
def on_click(event):
    # Chọn giá trị a
    if event.button is MouseButton.LEFT:
        global a
        a = abs(round(event.ydata) - yc)
        print("Value a = %d" % a)
    # Chọn giá trị b
    if event.button is MouseButton.RIGHT:
        global b
        b = abs(round(event.xdata) - xc)
        print("Value b = %d" % b)
        plt.disconnect(button_click)
        bres(xc, yc, a, b)

button_click = plt.connect('button_press_event', on_click)

plt.show()
