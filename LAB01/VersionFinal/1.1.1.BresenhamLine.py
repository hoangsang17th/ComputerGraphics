# Đã XONG
from tkinter import Tk, Canvas, Frame, BOTH

x1 = 0
x2 = 0
y1 = 0
y2 = 0
class Bresenham(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()
        
    def initUI(self):
        global x1, x2, y1, y2
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

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        print(xcoordinates)
        print(ycoordinates)
        canvas.create_line(x1, y1, x2, y2)

        canvas.pack(fill=BOTH, expand=1)

# def bres(x1, y1, x2, y2):
#     # Cho biến x = x1, y = y1
#     x, y = x1, y1
#     # Tính dx, dy bằng trị tuyệt đối
#     dx = abs(x2 - x1)
#     dy = abs(y2 - y1)
#     # Gọi m = dy/dx
#     m = dy/float(dx)
#     # Vì ở dây m được tính theo trị tuyệt đối của dx, dy nên ta không chia ra làm 8 trường hợp nữa
#     # Chỉ chia ra làm 2
#     # Nếu 0< m <=1 thì giữ nguyên
#     # Nếu m > 1 thì thay đổi cặp đối số
#     if m > 1:
#         dx, dy = dy, dx
#         x, y = y, x
#         x1, y1 = y1, x1
#         x2, y2 = y2, x2
#     # Khai báo biến p mặc định
#     p = 2 * dy - dx
#     xcoordinates = [x]
#     ycoordinates = [y]
#     # range hàm range(start, stop, step) với yêu cầu bắt buộc là stop
#     # Trong th này dx là biến stop
    
#     for k in range(dx):
#         if p > 0:
#             y = y + 1 if y < y2 else y - 1
#             p = p + 2 * (dy - dx)
#         else:
#             p = p + 2 * dy

#         x = x + 1 if x < x2 else x - 1

#         # print('x = %s, y = %s' % (x, y))
#         # append phương pháp gắn thêm 1 phần tử vào cuối mảng
#         xcoordinates.append(x)
#         ycoordinates.append(y)
#     # plt.ioff()
#     plt.get(x)
#     plt.plot(xcoordinates, ycoordinates)
#     # plt.grid(True)
#     plt.show()
def leftClick(event):
    global x1
    global y1
    x1 = round(event.x)
    y1 = round(event.y)
    print("X1, Y1: ", event.x, event.y)

def middleClick(event):
    print("Lạy trời cho em nó chạy:))")
    draw = Bresenham()

def rightClick(event):
    global x2
    global y2
    x2 = round(event.x)
    y2 = round(event.y)
    print("X2, Y2: ", event.x, event.y)
        

def main():
    
    root = Tk()
    root.title("Bresenham Line")
    
    # Trái lấy điểm đầu
    root.bind("<Button-1>", leftClick)
    # Giữa bắt đầu vẽ
    root.bind("<Button-2>", middleClick)
    # Phải lấy điểm cuối
    root.bind("<Button-3>", rightClick)
    root.geometry("750x350+400+200")
    root.mainloop()


if __name__ == '__main__':
    main()