#Write a Python program to change the position of every n-th value with the (n+1)th in a list.

def change_position(data):

    for x in range(0,len(data)):
        if(x != (len(data) - 1)):
            data[x] = data[x+1]

    return data

if __name__ == '__main__':
        
    l = int(input("Enter Length"))
    data = []

    for x in range(0,l):
        c = int(input("Enter number"))
        data.append(c)

    print(change_position(data))        

