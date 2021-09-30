# Đối xứng
import matplotlib.pyplot as plt
from numpy import *
import math
def reflection(x, y, a, b):
    xA = int(x)
    yA = int(y)
    aX = int(a)
    bX = int(b)
    # y = ax+b
    # ax - y + b = 0
    # y = (- x - c)/a 
    # x' + ay' + c = 0
    # Tìm ẩn số c của phương trình đường thẳng đi qua A và vuông góc với dt d
    c = - xA - aX * yA
    # Từ pt đường thăng trên tìm giao điểm của 2 dt
    xH = -(aX * bX + c) / (aX* aX + 1)
    yH = aX * xH + bX
    # # Lấy giá trị để vẽ đường thẳng cho trực quan hơn
    # xL = -100
    # yL = aX * xL + bX
    # yM = 100
    # xM = (yM - bX) / aX
    
    # xLine = [xL, xM]
    # yLine = [yL, yM]
    # plt.plot(xLine, yLine)
    # Vì Điểm H này là giao diemrd đồng thời cũng là trung điểm của AB nên
    xB = 2 * xH - xA
    yB = 2 * yH - yA
    # Vẽ thôi
    plt.scatter(xB, yB, s=100)
    # xO = 100
    # yO = 70
    # với góc 180
    # x = ([0,105,210,0]) 
    # y = ([0,210,0,0])
    #  abca
    # A 00
    # B 100 210
    # C 210 0

    

def main():
    plt.figure("Reflection :))")
    plt.title("Reflection 2D")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.plot(220, 220)
    plt.gcf().set_size_inches(6, 6)
    
    print("Tọa độ điểm A mà bạn muốn là A(x,y)")
    x = input("Bạn muốn x = ")
    y = input("bạn muốn y = ")
    plt.scatter(x, y, s=100)
    print("Đường thẳng đối xứng có tọa độ: Y = aX + b")
    a = input("Bạn muốn a = ")
    b = input("bạn muốn b = ")
    reflection(x, y, a, b)
    
    plt.show()
    
    

if __name__ == "__main__": main()
