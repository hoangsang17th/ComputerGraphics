# # Quay
import matplotlib.pyplot as plt
from numpy import *
import math
def rotation(x, y, rotationAngle):
    cosAngle = math.cos(int(rotationAngle)*(math.pi/180))
    sinAngle = math.sin(int(rotationAngle)*(math.pi/180))
    xO = int(x)
    yO = int(y)
    # xO = 100
    # yO = 70
    # với góc 180
    # x = ([0,105,210,0]) 
    # y = ([0,210,0,0])
    #  abca
    # A 00
    # B 100 210
    # C 210 0
    print(cosAngle)
    # x = ([
    #     (0-xO)*cosAngle- (0- yO)*sinAngle +xO,
    #     (105 -xO)*cosAngle- (105 - yO)*sinAngle +xO,
    #     (210 -xO)*cosAngle- (210 - yO)*sinAngle +xO,
    #     (0-xO)*cosAngle- (0- yO)*sinAngle +xO]) 
    # y = ([
    #     (0-xO)*sinAngle + (0- yO)*cosAngle +yO,
    #     (210 -xO)*sinAngle + (210 - yO)*cosAngle +yO,
    #     (0-xO)*sinAngle + (0- yO)*cosAngle +yO,
    #     (0-xO)*sinAngle + (0- yO)*cosAngle +yO])
    x = ([
        (0 - xO) * cosAngle - (0 - yO) * sinAngle + xO,
        (105 -xO) * cosAngle - (210 - yO) * sinAngle + xO,
        (210 -xO) * cosAngle - (0 - yO) * sinAngle + xO,
        (0 - xO) * cosAngle - (0 - yO) * sinAngle + xO]) 
    y = ([
        (0-xO)*sinAngle + (0 - yO) * cosAngle + yO,
        (105 -xO)*sinAngle + (210 - yO) * cosAngle + yO,
        (210-xO)*sinAngle + (0 - yO) * cosAngle + yO,
        (0-xO)*sinAngle + (0 - yO) * cosAngle + yO])
    plt.plot(x,y, color='red')
    

def main():
    plt.figure("Rotation :))")
    plt.title("Rotation 2D")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.plot(220, 220)
    plt.gcf().set_size_inches(6, 6)
    x = ([0,105,210,0]) 
    y = ([0,210,0,0])
    
    plt.plot(x,y)
    rotationAngle = input("Xoay hình góc X độ: ")
    xO = input("Tọa độ tâm X: ")
    yO = input("Tọa độ tâm Y: ")

    print(rotationAngle)
    rotation(xO, yO, rotationAngle)
    
    plt.show()
    
    

if __name__ == "__main__": main()
