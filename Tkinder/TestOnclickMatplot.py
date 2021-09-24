# Mô phỏng sự kiện click trong matplotlib
# Khỏi tạo giao diện
# Lắng nghe sự kiện click
# Sử lý dữ liệu từ click vừa này
# Thực hiện hàm tiếp theo
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10)
y = x**2

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y)

coords = []

def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print ('x = %d, y = %d' %(ix, iy))

    global coords
    coords.append((ix, iy))

    if len(coords) == 2:
        fig.canvas.mpl_disconnect(cid)

    return coords
cid = fig.canvas.mpl_connect('button_press_event', onclick)
# def bres(xc, yc , a):
#     print("Event click the point xc is %s" %xc)
#     print("Event click the point yc is %s" %yc)
    
# def main():
#     # a = int(input("Enter the point of b: "))
#     # plt.show()
#     fig.canvas.mpl_connect('button_press_event', onclick)
#     # bres(xc, yc, a)
    


# if __name__ == "__main__":
#     main()