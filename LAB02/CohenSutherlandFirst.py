# Đã XONG
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
plt.figure("Hoang Sang :))")
plt.title("CohenSutherland")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
# Tạo khung
plt.plot(200, 200)
# Tùy chỉnh size cửa sổ
plt.gcf().set_size_inches(10, 6)

# Khởi tạo tọa độ hình chữ nhật
xmin = 10
ymin = 10
xmax = 140
ymax = 90
xA = 50
yA = 120
xB = 175
yB = 50
c = 0
xdA = 0
xdB = 0
ydA = 0
ydB = 0

# Tạo hình chủ nhật
rectangle = plt.Rectangle((xmin, ymin), xmax, ymax)
# Thêm hình cũng nhật
plt.gca().add_patch(rectangle)

def code(x, y):
    global c
    c = 0
    if y > ymax: c=8
    if y < ymin: c=4
    if x > xmax: c=2
    if x < xmin: c=1
    
    return c

    
def cohenLine(xA, yA, xB, yB):
    global xdA, xdB, ydA, ydB, xmax, xmin, ymax, ymin
    
    # Tính c
    cA = 0
    if yA > ymax: cA=8
    if yA < ymin: cA=4
    if xA > xmax: cA=2
    if xA < xmin: cA=1
    
    cB = 0
    if yB > ymax: cB = 8
    if yB < ymin: cB = 4
    if xB > xmax: cB = 2
    if xB < xmin: cB = 1
    m = (yB - yA) / (xB - xA)
    print("Trước hàm white")
    while cA or cB > 0:
        # TH1: Điểm A và B nằm cùng phía
        if cA and cB != 0: 
            print(cA, cB)
            print("Trước hàm white")
            exit(0)
        
        # TH2: Điểm A hoặc B nằm trong hình
		# Hoán đổi A và B
        xi = xA
        yi = yA
        c = cA
        if c == 0:
            c=cB
            xi = xB
            yi = yB

        # TH3:
        # Tính tọa độ cắt với các cạnh hình chữ nhật
        if c == 8:
            y = ymax
            x = xi + 1 / m * (ymax - yi)
        elif c == 4:
            y = ymin
            x = xi + 1 / m * (ymin - yi)
        elif c == 2:
            x = xmax
            y = yi + m * (xmax - xi)
        elif c == 1:
            x = xmin
            y = yi + m * (xmin - xi)

        # Cập nhật lại tọa độ điểm A và B để vẽ lại đoạn thẳng
		# Tính ma diem A va B
        print("Trước hàm tính mã điểm A và B")
        if c == cA:
            xdA = x
            ydA = y
            cA = 0
            if ydA > ymax: cA=8
            if ydA < ymin: cA=4
            if xdA > xmax: cA=2
            if xdA < xmin: cA=1
            
        if c == cB:
            xdB = x
            ydB = y
            cB = 0
            if ydB > ymax: cB = 8
            if ydB < ymin: cB = 4
            if xdB > xmax: cB = 2
            if xdB < xmin: cB = 1

    print("Trước khi vẽ lần 2")
    x_values = [xA, xB]
    y_values = [yA, yB]
    print("xdA: %d, ydA: %d" % (xdA, ydA))
    print("xdB: %d, ydB: %d" % (xdB, ydB))
    # Mặc dù đã cố gắng nhưng mà vẫn có vấn đề với thuật toán
    plt.plot(x_values, y_values, color= "red")
    # plt.axline((xdA, ydA), (xdB, ydB), color= "red")
    plt.draw()

# Khâu xử lý sự kiện click không cần thay đổi
def on_click(event):
    global xA, yA, xB, yB
    # Click chuột trái để lấy giá trị xA, yA
    if event.button is MouseButton.LEFT:
        print('data coords %d %d' % (round(event.xdata), round(event.ydata)))
        xA = round(event.xdata)
        yA = round(event.ydata)
        print("xA: %d, yA: %d" % (xA, yA))
    # Click chuột phải để lấy giá trị xB, yB
    # Vui lòng click theo thứ tự chuột trái -> phải
    if event.button is MouseButton.RIGHT:
        xB = round(event.xdata)
        yB = round(event.ydata)
        print("xB: %d, yB: %d" % (xB, yB))

        plt.disconnect(button_click)
        # plt.close()
        cohenLine(xA, yA, xB, yB)


button_click = plt.connect('button_press_event', on_click)

plt.show()