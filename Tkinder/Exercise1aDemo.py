import matplotlib.pyplot as plt
plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def bres(x1, y1, x2, y2):
    # Khai báo 2 biến x, y lần lượt bằng x1 và y1
    x, y = x1, y1
    # Tính dx và dy bằng hàm trị tuyệt đối
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    # Tính m
    m = dy/float(dx)
    # Xét m
    # TH 0< m <=1
    if 0< m <= 1:
        # Khai báo p và xử lý p
        p = 2*dy - dx
        if p >= 0: 
            p = p + (2*dy - 2*dx)
            y = y + 1
        else: 
            p = p +2*dy
    if m>1: 
        y= y+ 1
    # Khai báo p mặc định 
    
    # print("x = %s, y = %s" % (x, y))
    # khởi tạo các điểm vẽ biểu đồ
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        print('x = %s, y = %s' % (x, y))
        xcoordinates.append(x)
        ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates)
    plt.show()


def main():
    x1 = int(input("Enter the starting point of x: "))
    y1 = int(input("Enter the starting point of y: "))
    x2 = int(input("Enter the end point of x: "))
    y2 = int(input("Enter the end point of y: "))

    bres(x1, y1, x2, y2)


if __name__ == "__main__":
    main()