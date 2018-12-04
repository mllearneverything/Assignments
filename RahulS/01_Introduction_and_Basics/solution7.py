#python3

def formString(string):

    if len(string) < 2:
        return

    if len(string) <= 3:
        return string

    return string[0:2]+string[-2:]


if __name__ == '__main__':

    string = input("Enter the string: ")

    newstring = formString(string)

    if newstring is not None:
        print (newstring)

    else:
        print ("length of string is smaller than minimum required")




