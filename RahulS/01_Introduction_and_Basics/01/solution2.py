#python3
import argparse

def summation(array):
    totalsum = 0
    for num in array:
        totalsum += num

    return totalsum



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as inp:
        array = map(int,inp.read().split()) 
        totalsum = summation(array)
        print (totalsum)


