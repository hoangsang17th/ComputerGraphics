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
# Thuật xén hình - Cắt đường thảng vào hình
# Những phần của đường thẳng không thuộc hình Chữ nhật thì xén (Làm mất nó)
# 1. Đoạn thẳng có 2 điểm đầu cuối nằm trong mặt phẳng => Không cần xén
# 2. Đoạn thẳng có 2 điểm đầu cuối cùng nằm ngoài một phía của mặt phẳng => Cả đoạn thẳng nằm ngoài mặt phẳng và cần xén
# 3. Đoạn thẳng cắt biên cửa sổ xén => Tìm giao điểm của đoạn thẳng với biên cửa sổ => Xén phần bên ngoài của sổ
# Thuật toán cohen chia mặt phẳng thành 8 phần
# Khởi tạo tọa độ hình chữ nhật
xmin = 10
ymin = 10
xmax = 140
ymax = 90
# Tọa độ đoạn thẳng AB mặc định
xA = 0
yA = 0
xB = 0
yB = 0

cA = 0
cB = 0

xdA = 0
xdB = 0
ydA = 0
ydB = 0

# Tạo hình chủ nhật
# Tọa độ xy, chiều dài, chiều rộng
rectangle = plt.Rectangle((xmin, ymin), (xmax - xmin), (ymax - ymin))
# Thêm hình cũng nhật
plt.gca().add_patch(rectangle)

# Chỗ này làm sai
def codeX(x, y):
    code = 0
    if x < xmin: code = 1
    if x > xmax: code = 2
    if y > ymax: code = 4
    if y < ymin: code = 8
    return code

    
def cohenLine(xA, yA, xB, yB):
    global xdA, xdB, ydA, ydB, xmax, xmin, ymax, ymin, cA, cB
    
    # Xác định ví trí của điểm xA, yA trên mặt phẳng
    cA = codeX(xA, yA)
    print("cA :", cA)

    # Xác định ví trí của điểm xB, yB trên mặt phẳng
    cB = codeX(xB, yB)
    print("cB :",cB)
    # Trở lên vẫn đúng
    x_values = [xA, xB]
    y_values = [yA, yB]
    # 1. cA = cB = 0. Đoạn thẳng là chính nó vì nó nằm bên trong hình xén
    # Vẽ đoạn thẳng và kết thúc bài toán.
    if cB == cA == 0:
        print("cB == 0 & cA == 0")
        # Vẽ luôn khỏi cần xử lý, màu xanh chứng tỏ đã được xén
        plt.plot(x_values, y_values, color= "red")
        plt.draw()
    # 2. cA = cB và cA != 0. Đoạn thẳng nằm bên ngoài biên của sổ. 
    # Kết thúc bài toán
    if cA == cB & cA != 0:
        # Vẽ luôn khỏi cần xử lý, màu đỏ chứng tỏ đã được xén nhưng không được vẻ
        print("cA == cB & cA != 0")
        plt.plot(x_values, y_values, color= "blue")
        plt.draw()

    # 3. cA và cB không thuộc 2 trường hợp trên
    # 
    else:
        m = (yB - yA) / (xB - xA)
        xdA, xdB, ydA, ydB = xA, xB, yA, yB
        if cA == 1: 
            ydA = yA + m * (xmin - xA)
            xdA = xmin
        if cA == 2: 
            ydA = yA + m * (xmax - xA)
            xdA = xmax
        if cA == 4:
            xdA = xA + m * (ymax - yA)
            ydA = ymax
        if cA == 8:
            xdA = xA + m* (ymin - yA)
            ydA = ymin

        if cB == 1: 
            ydB = yB + m * (xmin - xB)
            xdB = xmin
        if cB == 2: 
            ydB = yB + m * (xmax - xB)
            xdB = xmax
        if cB == 4:
            xdB = xB + m * (ymax - yB)
            ydB = ymax
        if cB == 8:
            xdB = xB + m* (ymin - yB)
            ydB = ymin
        
        print("xdA: %d, ydA: %d" % (xdA, ydA))
        print("xdB: %d, ydB: %d" % (xdB, ydB))
        # plt.plot((xa, ya), (xb, yb), color= "red")
        plt.plot((xdA, xdB), (ydA, ydB), color= "red")
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
        # Ngắt kết nối sự kiện click chuột
        plt.disconnect(button_click)
        # Gọi hàm và bắt đầu tính toán dựa trên 2 dữ liệu đã có từ việc click chuột
        cohenLine(xA, yA, xB, yB)


button_click = plt.connect('button_press_event', on_click)

plt.show()