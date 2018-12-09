
# usage: Sol_4.py [-h] n

# positional arguments:
#   n           n to find n + nn + nnn

# optional arguments:
#   -h, --help  show this help message and exit

import math
import argparse

def computeEquation(n):
    return n + pow(n, 2) + pow(n, 3)
   
    
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="n to find n + nn + nnn", type=int)
    args = parser.parse_args()

    print("n + nn + nnn: {}".format(computeEquation(args.n)))

if __name__ == "__main__":
    Main()