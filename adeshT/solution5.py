#Write a Python program to test whether a passed letter is a vowel or not.

def Is_Vowel_or_Not(letter):
	if(letter == 'a' or letter == 'e'or letter == 'i' or letter == 'o' or letter == 'u'):
		return True
	else:
		return False	

if __name__ == '__main__':

	letter = input()
	print(Is_Vowel_or_Not(letter))
