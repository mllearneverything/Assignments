#python3

def secondSmallest(numlist):

    smallest = numlist[0]
    secondsmallest  = smallest

    for i in range(len(numlist)):
        if numlist[i] < smallest:
            secondsmallest = smallest
            smallest = numlist[i]

        elif numlist[i] < secondsmallest: 
            secondsmallest = numlist[i]

    return secondsmallest


if __name__ == '__main__':

    numlist = [10, 20, 15]
    print (("second smallest element in list is %d") % (secondSmallest(numlist)))


