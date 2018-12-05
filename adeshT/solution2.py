#Write a Python program which accepts the users first and last name and print them in reverse order with a space between them.


def reverse_name(first_name,last_name):
    first = first_name[::-1]
    last  = last_name[::-1]
    return (first + " " + last)


first_name = input()
last_name = input()
print(reverse_name(first_name,last_name))	 

    