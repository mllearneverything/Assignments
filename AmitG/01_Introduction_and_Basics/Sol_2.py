# Find area of circle.
# usage: Sol_2.py [-h] radius
# positional arguments:
# radius      radius of circle

# optional arguments:
#   -h, --help  show this help message and exit

import math
import argparse

def computeArea(radius):
    return math.pi * pow(radius, 2)
   
    
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("radius", help="radius of circle", type=int)
    args = parser.parse_args()

    print("Area of circle: {}".format(computeArea(args.radius)))

if __name__ == "__main__":
    Main()