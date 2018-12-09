#python3
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as inp:
        array = list(map(int,inp.read().split()))
        print (("number of 4's is: %d") % (array.count(4)))



