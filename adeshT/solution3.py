#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

def compute(num):
	return (n + (n*n) + (n*n*n))

if __name__ == '__main__':
	
	num = int(input())
	print(compute(num))
