#python3

def findlargest(numlist):

    largest = numlist[0]

    for i in range(len(numlist)):
        if numlist[i] > largest:
            largest = numlist[i]

    return largest


if __name__ == '__main__':

    numlist = [2,35,1,53,56,2,6,9,5,42]
    print (("largest element in list is %d") % (findlargest(numlist)))


