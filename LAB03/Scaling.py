# Tỉ lệ
import matplotlib.pyplot as plt

def scaling(xA, yA, sX, sY):
    xO = 40/2 + xA
    yO = 40/2 + yA
    x = xO - (40 * int(sX))/2  
    y = yO - (40 * int(sY))/2
    rectangleT = plt.Rectangle((x, y), 40 * int(sX), 40 * int(sY), color='red')
    plt.gca().add_patch(rectangleT)
    plt.draw()
    

def main():
    plt.figure("Scaling :))")
    plt.title("Scaling 2D")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.plot(200, 200)
    plt.gcf().set_size_inches(6, 6)
    xA = 10
    yA = 10
    rectangle = plt.Rectangle((xA, yA), 40, 40)
    sX = input("Tỉ lệ sX đơn vị: ")
    print(sX)
    sY = input("Tỉ lệ sY đơn vị: ")
    scaling(xA, yA, sX, sY)
    plt.gca().add_patch(rectangle)
    
    plt.show()
    
    

if __name__ == "__main__": main()
