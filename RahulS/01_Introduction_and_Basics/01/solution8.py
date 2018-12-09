#python3
import argparse

def findlargest(numlist):

    largest = numlist[0]

    for i in range(len(numlist)):
        if numlist[i] > largest:
            largest = numlist[i]

    return largest



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as inp:
        array = list(map(int,inp.read().split()))
        print (("largest element in list is %d") % (findlargest(array)))


