#python3
import argparse

def swap(numlist):

    i = 0
    while(i < len(numlist)-1):
        temp = numlist[i+1]
        numlist[i+1] = numlist[i]
        numlist[i] = temp
        i += 2

    return numlist

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as inp:
        array = list(map(int,inp.read().split()))
        numlist = swap(array)
        print ("after swapping list is \n", numlist)


