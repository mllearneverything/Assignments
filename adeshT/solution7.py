#Write a Python program to get the largest number from a list

def largest(list):
	return max(list)

if __name__ == '__main__':
	
    data = []
    l = input("Enter length of list")
    for x in range(0,l):
        print("Enter element")
        c = int(input())
        data.append(c)
    print(largest(l))	