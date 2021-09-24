from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy
# t = np.arange(0.0, 1.0, 0.01)
# s = np.sin(2 * np.pi * t)
# plt.subplots()
plt.imshow(numpy.zeros((500, 500)), "Blues")

def midpoint(xc, yc, r):
    x = 0
    y = r
    # Giá trị p tại điểm dầu tiên (0, r) có giá trị p =5/4 -r
    p = 5/4 -r
    data = numpy.zeros((500, 500)) 
    while x < y:
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
            p = p + 2*x + 3
        else: 
            p = p + 2*(x-y) + 5
            y = y - 1
            
        x = x + 1
        
    plt.imshow(data, "Blues")
    plt.draw()   


def on_click(event):
    if event.button is MouseButton.LEFT:
        print('data coords %f %f' % (round(event.xdata), round(event.ydata)))
        plt.disconnect(button_click)

        midpoint(round(event.ydata), round(event.xdata), 100)
            



button_click = plt.connect('button_press_event', on_click)

plt.show()