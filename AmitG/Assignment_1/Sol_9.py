# usage: Sol_9.py [-h] numbers [numbers ...]

# positional arguments:
#   numbers     list of numbers

import math
import argparse

def min2OfElements(numbers):
    min = numbers[0]
    min2 = numbers[1] 
    for i in range(1, len(numbers)):
        if numbers[i] < min:
            min2 = min
            min = numbers[i]
        elif numbers[i] < min2:
            min2 = numbers[i]
    return min2

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", help="list of numbers", nargs="+", type=int)
    args = parser.parse_args()

 
    print("2nd minimum number in list : {}".format(min2OfElements(args.numbers)))

if __name__ == "__main__":
    Main()