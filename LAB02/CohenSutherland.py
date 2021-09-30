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
    if x < xmin: 
        code = 1
        if y < ymin: code = 5
        if y > ymax: code = 9
        
    if x > xmax: 
        code = 2
        if y < ymin: code = 6
        if y > ymax: code = 10

    if y < ymin: 
        code = 4
        if x < xmin: code = 5
        if x > xmax: code = 6
    if y > ymax: 
        code = 8
        if x < xmin: code = 9
        if x > xmax: code = 10
    
    return code

def equationX(x, y):
    print(xA, yA, xB, yB)
    value = 0
    value = (yB - yA) * (x - xA) + (xB -xA) * (y - yA)
    return value

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
    # Phần phía dưới sẽ làm chi tiết phần này hơn
    # if cA == cB & cA != 0:
    #     # Vẽ luôn khỏi cần xử lý, màu đỏ chứng tỏ đã được xén nhưng không được vẻ
    #     print("cA == cB & cA != 0")
    #     plt.plot(x_values, y_values, color= "blue")
    #     plt.draw()
    # Để phân rõ hơn, ta bắt đầu đưa ra nhiều trường hợp hơn để xén hình đạt kết quả tốt hơn
    # Trường hợp cả đoạn thẳng nằm ở phía trên hình xén
    elif (cA==8 or cA == 9 or cA == 10) and (cB == 8 or cB == 10 or cB == 9):
        print("Helllo")
        plt.plot(x_values, y_values, color= "blue")
        plt.draw()

    # Trường hợp cả đoạn thẳng nằm ở phía bên trái hình xén
    elif (cA==1 or cA == 5 or cA == 9) and (cB == 1 or cB == 5 or cB == 9):
        plt.plot(x_values, y_values, color= "blue")
        plt.draw()

    # Trường hợp cả đoạn thẳng nằm ở phía bên phải hình xén
    elif (cA==10 or cA == 2 or cA == 6) and (cB == 10 or cB == 2 or cB == 6):
        plt.plot(x_values, y_values, color= "blue")
        plt.draw()
    
    # Trường hợp cả đoạn thẳng nằm ở phía bên dưới hình xén
    elif (cA==4 or cA == 5 or cA == 6) and (cB == 4 or cB == 5 or cB == 6):
        plt.plot(x_values, y_values, color= "blue")
        plt.draw()
    # 3. cA và cB không thuộc 2 trường hợp trên
    # 
    else:
        # Hệ số góc
        m = (yB - yA) / (xB - xA)
        print("Hệ số góc m: ", m)
        xdA, xdB, ydA, ydB = xA, xB, yA, yB
        if cA == 1: 
            ydA = yA + m * (xmin - xA)
            xdA = xmin
        if cA == 2: 
            ydA = yA + m * (xmax - xA)
            xdA = xmax
        if cA == 4:
            xdA = xA + (ymin - yA) / m
            ydA = ymin
        if cA == 5:
            # Phải xét xem hắn là 1 hay 4 hay cả hai
            # Chỗ ca này cu hơi gấp
            
            xdA = xA + (ymin - yA) / m
            ydA = yA + m * (xmin - xA)

        if cA == 6:
            xdA = xmax
            ydA = yA + m * (xmin - xA)
        if cA == 8:
            xdA = xA + (ymax - yA) / m 
            ydA = ymax
        if cA == 9:
            xdA = xmin
            ydA = ymax
        if cA == 10:
            # Gọi 2 điểm L và G với L(xmax, ymax) và G((xmax-xmin)/2, (ymax+10))
            l = equationX(xmax, ymax)
            g = equationX(75, 125)
            print(l, g)
            ydA = yA + m * (xmax - xA)
            xdA = xmax
            # xdA = xmax
            # ydA = ymax

        # if cB == 1: 
        #     ydB = yB + m * (xmin - xB)
        #     xdB = xmin
        # if cB == 2: 
        #     ydB = yB + m * (xmax - xB)
        #     xdB = xmax
        # if cB == 4:
        #     xdB = xB + m * (ymax - yB)
        #     ydB = ymax
        # if cB == 8:
        #     xdB = xB + m* (ymin - yB)
        #     ydB = ymin
        if cB == 1: 
            ydB = yB + m * (xmin - xB)
            xdB = xmin
        if cB == 2: 
            ydB = yB + m * (xmax - xB)
            xdB = xmax
        if cB == 4:
            xdB = xB + (ymin - yB) / m
            ydB = ymin
        if cB == 5:
            xdB = xB + (ymin - yB) / m
            ydB = ymin
        if cB == 6: 
            ydB = ymin
            xdB = xmax
        if cB == 8: 
            ydB = ymax
            xdB = xB + (ymax - yB) / m
        if cB == 9:
            xdB = xmin
            ydB = ymax
        if cB == 10:
            xdB = xmax
            ydB = ymax
        
        print("xdA: %d, ydA: %d" % (xdA, ydA))
        print("xdB: %d, ydB: %d" % (xdB, ydB))
        x_values = [xdA, xdB]
        y_values = [ydA, ydB]
        plt.plot(x_values, y_values, color= "red")
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