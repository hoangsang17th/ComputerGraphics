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

    
def binaryLine(xA, yA, xB, yB):
    global xdA, xdB, ydA, ydB, xmax, xmin, ymax, ymin, cA, cB
    
    # Xác định ví trí của điểm xA, yA trên mặt phẳng
    cA = codeX(xA, yA)
    
    # Xác định ví trí của điểm xB, yB trên mặt phẳng
    cB = codeX(xB, yB)
    # Trở lên vẫn đúng
    x_values = [xA, xB]
    y_values = [yA, yB]
    # 1. cA = cB = 0. Đoạn thẳng là chính nó vì nó nằm bên trong hình xén
    # Vẽ đoạn thẳng và kết thúc bài toán.
    if (cB | cA ) == 0:
        # Vẽ luôn khỏi cần xử lý, màu xanh chứng tỏ đã được xén
        plt.plot(x_values, y_values, color= "red")
        plt.show()
    # 2. cA = cB và cA != 0. Đoạn thẳng nằm bên ngoài biên của sổ. 
    # Kết thúc bài toán
    if (cA & cB ) != 0:
        # Vẽ luôn khỏi cần xử lý, màu đỏ chứng tỏ đã được xén nhưng không được vẻ
        plt.plot(x_values, y_values, color= "blue")
        plt.show()

    # 3. cA và cB không thuộc 2 trường hợp trên
    # 
    m = (yB - yA) / (xB - xA)
    if cA !=0 & cB == 0: 
        # Hoán đổi A B
        swap = cA
        cA = cB
        cB = swap
    if cA ==0 & cB != 0:
        xdA = xA
        ydA = yA
        xdB = xB
        ydB = yB
        while abs(xdA - xdB) +abs(ydA - ydB) >2:
            xM = (xdA + xdB) / 2
            yM = (ydA + ydB) / 2
            cM = codeX(xM, yM)
            if cM == 0:
                xdA = xM
                ydA = yM
            else:
                ydB = yM
                xdB = xM
    
    # Xong vong lặp thì vẽ và hiển thị
    plt.plot([xA, xdA], [yA, ydA], color= "blue")
    plt.show()

    if (cA !=0 & cB != 0) & (cA & cB) == 0:
        xdA = xA
        ydA = yA
        xdB = xB
        ydB = yB
        xM = (xdA + xdB) / 2
        yM = (ydA + ydB) / 2
        cM = codeX(xM, yM)
        while cM !=0 & (abs(xdA - xdB) +abs(ydA - ydB)) >2:
            cP = codeX(xdA, ydA)
            if (cP & cM) != 0:
                xdA = xM
                ydA = yM
            else:
                xdB = xM
                ydB = yM
            
            xM = (xdA + xdB) / 2
            yM = (ydA + ydB) / 2
        
        if cM == 0:
            # Xong vong lặp thì vẽ và hiển thị
            plt.plot([xdA, xM], [ydA, yM], color= "blue")
            plt.plot([xM, xdB], [yM, ydA], color= "blue")
            plt.show()



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
        binaryLine(xA, yA, xB, yB)


button_click = plt.connect('button_press_event', on_click)

plt.show()
