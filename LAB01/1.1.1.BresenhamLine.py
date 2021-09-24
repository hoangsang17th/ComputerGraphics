# Đã XONG
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt

plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.plot(300, 300)

def bres(x1, y1, x2, y2):
    # Cho biến x = x1, y = y1
    x, y = x1, y1
    # Tính dx, dy bằng trị tuyệt đối
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    # Gọi m = dy/dx
    m = dy/float(dx)
    # Vì ở dây m được tính theo trị tuyệt đối của dx, dy nên ta không chia ra làm 8 trường hợp nữa
    # Chỉ chia ra làm 2
    # Nếu 0< m <=1 thì giữ nguyên
    # Nếu m > 1 thì thay đổi cặp đối số
    if m > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    # Khai báo biến p mặc định
    p = 2 * dy - dx
    xcoordinates = [x]
    ycoordinates = [y]
    # range hàm range(start, stop, step) với yêu cầu bắt buộc là stop
    # Trong th này dx là biến stop
    
    for k in range(dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        # print('x = %s, y = %s' % (x, y))
        # append phương pháp gắn thêm 1 phần tử vào cuối mảng
        xcoordinates.append(x)
        ycoordinates.append(y)
    # plt.ioff()
    plt.get(x)
    plt.plot(xcoordinates, ycoordinates)
    # plt.grid(True)
    plt.draw()

x1 = 0
x2 = 0
y1 = 0
y2 = 0

def on_click(event):
    # Click chuột trái để lấy giá trị x1, y1
    if event.button is MouseButton.LEFT:
        global x1
        global y1
        print('data coords %d %d' % (round(event.xdata), round(event.ydata)))
        x1 = round(event.xdata)
        y1 = round(event.ydata)
        print(x1, y1)
    # Click chuột phải để lấy giá trị x2, y2
    # Vui lòng click theo thứ tự chuột trái -> phải
    if event.button is MouseButton.RIGHT:
        x2 = round(event.xdata)
        y2 = round(event.ydata)
        print(x2, y2)
        plt.disconnect(button_click)
        # plt.close()
        bres(x1, y1, x2, y2)


button_click = plt.connect('button_press_event', on_click)

plt.show()