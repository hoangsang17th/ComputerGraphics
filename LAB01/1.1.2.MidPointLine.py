from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
plt.title("Midpoint Line Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.plot(300, 300)

def midpoint(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    
    d = dy - (dx/2)
    x = x1
    y = y1

    print('x = %s, y= %s' % (x, y))
    xcoordinates = [x]
    ycoordinates = [y]

    while(x < x2):
        x = x + 1
        if (d < 0):
            d = d + dy

        else:
            d = d + (dy - dx)
            y = y + 1

        xcoordinates.append(x)
        ycoordinates.append(y)
        # print('x =%s, y =%s' % (x, y))
    plt.plot(xcoordinates, ycoordinates)
    plt.draw()

x1 = 0
x2 = 0
y1 = 0
y2 = 0

def on_click(event):
    
    if event.button is MouseButton.LEFT:
        global x1
        global y1
        print('data coords %d %d' % (round(event.xdata), round(event.ydata)))
        x1 = round(event.xdata)
        y1 = round(event.ydata)
        print(x1, y1)
      
    if event.button is MouseButton.RIGHT:
        x2 = round(event.xdata)
        y2 = round(event.ydata)
        print(x2, y2)
        plt.disconnect(button_click)
        # plt.close()
        midpoint(x1, y1, x2, y2)


button_click = plt.connect('button_press_event', on_click)

plt.show()