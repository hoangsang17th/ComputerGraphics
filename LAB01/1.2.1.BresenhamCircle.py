# Đã xong
import matplotlib.pyplot as plt
import numpy
from matplotlib.backend_bases import MouseButton
# Tính bán kính vòng tròn
# r = math.sqrt((x-xc)*(x-xc) +(y-yc)*(y-yc))
plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.imshow(numpy.zeros((500, 500)), "Blues")

def bres(xc, yc, r):
    x = 0
    y = r
    # Giá trị p tại điểm dầu tiên (0, r) có giá trị p =3-2r
    p = 3 - 2 * r
    data = numpy.zeros((500, 500)) 
    while x < y:
        # draw(xc, yc, x, y)
        
        data[x+xc, y+yc]=1
        data[y+xc, x+yc]=1
        data[y+xc, -x+yc]=1
        data[x+xc, -y+yc]=1
        data[-x+xc, -y+yc]=1
        data[-y+xc, -x+yc]=1
        data[-y+xc, x+yc]=1
        data[-x+xc, y+yc]=1
        #   Thuật toán trang 22 CG.2.2D
        if p < 0:
            p = p + 4*x + 6
        else: 
            p = p + 4*(x-y) + 10
            y = y - 1
            
        x = x + 1
    # Tại sao lại là imshow mà không phải plot
    # imshow được sử dụng để đọc dữ liệu từ 1 mảng
    plt.imshow(data, "Blues")
    plt.draw()
            
    
    

def on_click(event):
    
    if event.button is MouseButton.LEFT:
        print('data coords %d %d' % (round(event.xdata), round(event.ydata)))
        yc = round(event.xdata)
        xc = round(event.ydata)
        bres(xc, yc, 100)


button_click = plt.connect('button_press_event', on_click)

plt.show()