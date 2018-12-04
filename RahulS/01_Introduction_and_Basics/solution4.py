#python3

def calculate(n):

    return (n + n*n + n*n*n)

if __name__ == '__main__':

    n = int(input("Enter the number: "))
    print (("value is: %d") % (calculate(n)))


