#python3

def summation(array):
    totalsum = 0
    for num in array:
        totalsum += num

    return totalsum



if __name__ == '__main__':

    array = (3,2,5,6,17,90,124,4323)
    totalsum = summation(array)
    print (totalsum)


