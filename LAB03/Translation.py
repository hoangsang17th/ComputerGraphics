import matplotlib.pyplot as plt

def translation(xA, yA, xB, yB):
    x = xA + int(xB)
    y = yA + int(yB)
    rectangleT = plt.Rectangle((x, y), 40, 40, color='red')
    plt.gca().add_patch(rectangleT)
    plt.draw()
    

def main():
    plt.figure("Translation :))")
    plt.title("Translation 2D")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.plot(200, 200)
    plt.gcf().set_size_inches(10, 6)
    xA = 10
    yA = 10
    rectangle = plt.Rectangle((xA, yA), 40, 40)
    xB = input("Tịnh tiến HCN x đơn vị: ")
    print(xB)
    yB = input("Tịnh tiến HCN y đơn vị: ")
    translation(xA, yA, xB, yB)
    plt.gca().add_patch(rectangle)
    
    plt.show()
    
    

if __name__ == "__main__": main()
