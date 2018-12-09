# usage: Sol_6.py [-h] char

# positional arguments:
#   char        char to check vowel or not

# optional arguments:
#   -h, --help  show this help message and exit
# import argparse

def isVowel(char):
    if char in 'aeiuo':
        return True
    else:
        return False

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('char', help='char to check vowel or not', type=str)
    args = parser.parse_args()
 
    if isVowel(args.char):
        print("Entered char is vowel")
        return
    print("Entered char is not vowel")
    return

if __name__ == '__main__':
    Main()