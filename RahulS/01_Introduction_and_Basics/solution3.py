#python3

if __name__ == '__main__':

    name = input("Enter your name with firstname and lastname: ")

    print (" ".join(name.split(" ")[::-1]))

