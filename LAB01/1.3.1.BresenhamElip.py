# Đã xong
import matplotlib.pyplot as plt
import numpy
import math
from matplotlib.backend_bases import MouseButton

plt.title("Bresenham Algorithm- Elip")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.imshow(numpy.zeros((500, 500)), "Blues")
# Từ bài 1.3.1 tất cả thuật toán đều được mô phỏng theo 
# thuật toán có sẵn trong slide bằng ngôn ngữ C++ của cô
def bres(xc, yc, a , b):
    a2 = a * a
    b2 = b * b
    x = 0
    y = b
    # Giá trị p tại điểm dầu tiên (0, r) có giá trị
    p =  -2 * b + 1 + 2*b2/a2
    x0 = a2/(math.sqrt(a2+b2))
    y0 = b2/(math.sqrt(a2+b2))
    data = numpy.zeros((500, 500)) 
    # Phía dưới hàm này cô gõ sai hàm
    while x < x0:
        # Hàm này cố định cho hình Elip
        data[x+xc, y+yc]=1
        data[x+xc, -y+yc]=1
        data[-x+xc, -y+yc]=1
        data[-x+xc, y+yc]=1
        
        if p < 0:
            p = p + 2*b2*(2*x+3)/a2
        else: 
            p = p + 4*(1-y) + 2*b2*(2*x+3)/a2
            y = y - 1
            
        x = x + 1
    
    x = a 
    y = 0
    p = 2 * a2/b2 -2*a+1
    while y < y0:
        # Hàm này cố định cho hình Elip
        data[x+xc, y+yc]=1
        data[x+xc, -y+yc]=1
        data[-x+xc, -y+yc]=1
        data[-x+xc, y+yc]=1
        
        if p < 0:
            p = p + 2*a2*(2*y+3)/b2
        else: 
            p = p + 4*(1-x) + 2*a2*(2*y+3)/b2
            x = x - 1
            
        y = y + 1
        
    
    plt.imshow(data, "Blues")
    # plt.show(block=False)
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
        print("123")
        bres(xc, yc, a, b)
    
    

button_click = plt.connect('button_press_event', on_click)

plt.show()

