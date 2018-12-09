# usage: Sol_7.py [-h] string

# positional arguments:
#   string      string to return string of first 2 and last 2 chars

# optional arguments:
#  -h, --help  show this help message and exit

import argparse

def returnString(string):    
    if len(string) < 2:
        return ""
    return (string[0:2]+string[-2:])

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('string', help='string to return string of first 2 and last 2 chars')
    args = parser.parse_args()

    print(returnString(args.string))
if __name__ == '__main__':
    Main()   