#python3
import argparse

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
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as inp:
        array = list(map(int,inp.read().split())) 
        print (("second smallest element in list is %d") % (secondSmallest(array)))


