# usage: Sol_3.py [-h] name

# positional arguments:
#   name        Firstname and lastname of user with space between them

# optional arguments:
#  -h, --help  show this help message and exit

import argparse

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Firstname and lastname of user with space between them', type=str)
    args = parser.parse_args()

    print(' '.join(args.name.split(' ')[::-1]))

if __name__ == '__main__':
    Main()