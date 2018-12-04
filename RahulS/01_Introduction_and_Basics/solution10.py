#python3

def swap(numlist):

    i = 0
    while(i < len(numlist)-1):
        temp = numlist[i+1]
        numlist[i+1] = numlist[i]
        numlist[i] = temp
        i += 2

    return numlist

if __name__ == '__main__':

    numlist = [x for x in range(1,100)]
    numlist = swap(numlist)
    print ("after swapping list is \n", numlist)


