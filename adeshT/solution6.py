#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string


def get_string(str):
	length = len(str)
	if(length < 2):
		return str
	else:
		first = str[0] + str[1]
		last  = str[length-2] + str[length-1]
		first = first + last
		return first

if __name__ == '__main__':
	
	str = input()
	print(get_string(str))
				
