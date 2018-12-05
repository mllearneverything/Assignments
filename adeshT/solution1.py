#Given an array of integers, find the sum of its elements.

def sum(arr):
    total = 0
    for x in arr:
        total = total + x
    return total

arr = (1,2,3,4,5)
p = sum(arr)
print(p)


	
	