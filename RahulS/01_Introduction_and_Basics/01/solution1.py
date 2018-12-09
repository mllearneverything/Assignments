#python3

def area(radius):

    return (radius*radius*(22/7))/1.0

if __name__ == '__main__':

    radius = float(input("Enter the radius: "))
    print (("area is: %.4f") % (area(radius)))


