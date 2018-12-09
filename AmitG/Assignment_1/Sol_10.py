# usage: Sol_10.py [-h] numbers [numbers ...]

# positional arguments:
#   numbers     list of numbers

import math
import argparse

def replace_n_with_n1(numbers):
    temp = numbers[0]
    for i in range(0, len(numbers)-1):
        numbers[i] = numbers[i+1]
    numbers[-1] = temp

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", help="list of numbers", nargs="+", type=int)
    args = parser.parse_args()
    replace_n_with_n1(args.numbers)
    print("Updated list: {}".format(args.numbers))

if __name__ == "__main__":
    Main()