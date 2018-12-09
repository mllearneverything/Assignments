#usage: Sol_5.py [-h] numbers [numbers ...]
#
#positional arguments:
#  numbers     list of numbers

#optional arguments:
#  -h, --help  show this help message and exit

import math
import argparse

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", help="list of numbers", nargs="+", type=int)
    args = parser.parse_args()


    print("number of 4 in list: {}".format(args.numbers.count(4)))

if __name__ == "__main__":
    Main()