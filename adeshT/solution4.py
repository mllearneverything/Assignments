#Write a Python program to count the number 4 in a given list.

def count_four(l):
    count = 0
    for element in l:
        if element == '4':
            count = count + 1
    return count
	
if __name__ == '__main__':
	
	l = list(input())
	print(count_four(l))			
