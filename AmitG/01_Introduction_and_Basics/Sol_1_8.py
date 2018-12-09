# Find sum of numbers.
#usage: Sol_1.py [-h] [-sum | -max | -min] numbers [numbers ...]

#positional arguments:
#  numbers      list of numbers

#optional arguments:
#  -h, --help   show this help message and exit
#  -sum, --sum  Find sum of numbers
#  -max, --max  Find max of numbers
#  -min, --min  Find min of numbers

import argparse

def sumOfElements(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

def minOfElements(numbers):
    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i
    return min

def maxOfElements(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max
    
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", help="list of numbers", nargs="+", type=int)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-sum", "--sum", help="Find sum of numbers", action="store_true")
    group.add_argument("-max", "--max", help="Find max of numbers", action="store_true")
    group.add_argument("-min", "--min", help="Find min of numbers", action="store_true")
    args = parser.parse_args()

    if args.max:
        print("Max of numbers: {}".format(maxOfElements(args.numbers)))
    elif args.min:
        print("Min of numbers: {}".format(minOfElements(args.numbers)))
    else:
        print("Sum of numbers: {}".format(sumOfElements(args.numbers)))

if __name__ == "__main__":
    Main()