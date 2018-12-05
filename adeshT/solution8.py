#Write a Python program to find the second smallest number in a list.

def sec_min(data):
    x = min(data)
    data.remove(x)
    x = min(data)
    return x

if __name__ == '__main__':

    l = int(input("Enter Length"))
    data = []

    for x in range(0,l):
        c = int(input("Enter number"))
        data.append(c)

    print(sec_min(data))

    


