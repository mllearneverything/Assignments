#python3

def IsVowel(letter):

    vowelList = ['a','e','i','o','u']

    if letter in vowelList:
        return True

    return False

if __name__ == '__main__':

    letter = input("Enter the letter: ")

    print("letter is vowel") if IsVowel(letter) else print("letter is not vowel")



