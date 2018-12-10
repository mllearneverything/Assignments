a = [4,12,8,6]
print sum(a)

def Area(a):
    area = 3.14*a*a
    print(area)

def First_Last(x,y):
    z = x+" "+y
    print(''.join(reversed(z)))

def Compute(n):
    c = n+n*n+n*n*n
    print(c)

def CountNumber(p):
    l = [4,12,4,6,4]
    return l.count(p)
    
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

def F2_L2(string):
    if len(string) < 2 :
        return ''
    return string[:2]+string[-2:]

def Max_Value_inList():
    l = [4,12,4,6,4]
    return max(l)

def Second_Smallest():
    l = [4,12,8,6]
    l.sort()
    return l[1]

#def Change_Position():
#    l = [4,12,8,6]
#    l.insert(0,l[-1])
#    l.pop(-1)
#    print(l)

def Change_Pos():
    l = [4,12,8,6,7]
    length = len(l)
    print(length)
    if 0 != length % 2:
        length = length - 1
    while i < length:
        temp = l[i]
        l[i] = l[i+1]
        l[i+1] = temp
        i += 2
    print(l)
    
def main():
    Area(3)
    First_Last('Pankaj', 'Patil')
    Compute(2)
    print(CountNumber(4))
    print(is_vowel('i'))
    print(is_vowel('p'))
    print(F2_L2('Pankaj'))
    print(Max_Value_inList())
    print(Second_Smallest())
    #Change_Position()
    Change_Pos()
    
if __name__ == '__main__':
  main()
