import math
#n = int(input())
n = 1234
i=0
j = len(str(n))

a = n % (10**(i+1))
b = math.floor((n % (10**(i+1)))/(10**(i)))
print("a is " + str(a))
print("b is " + str(b))
"""
if i == 0:
    if a % 2 == 0:
        print("The first digit is even")
        n = n - a
        print(n)
    else:
        print("The first digit is odd")
else:
    if b % 2 == 0:
        print("The " + str(i+1) +"th digit is even")
        #print(b*10**i)
        n = n - b*10**i
        print(n)
    else:
        print("The " + str(i+1) +"th digit is odd")
        print(n)
"""
"""    
for i in range(i, j - 1, 1):
    print("loop number "+ str(i+1))

    if i == 0:
        if a % 2 == 0:
            print("The first digit is even")
            n = n - a
            print(n)
        else:
            print("The first digit is odd")
        i=i+1
    else:
        if b % 2 == 0:
            print("The " + str(i+1) +"th digit is even")
            n = n - a*10**i+1
            print(n)
        else:
            print("The " + str(i+1) +"th digit is odd")
            print(n)
        i= i+1
"""        
for i in range(i, j, 1):
    print("loop number "+ str(i+1))
    if i == 0:
        if a % 2 == 0:
            print("The first digit is even")
            n = n - a
            print(n)
        else:
            print("The first digit is odd")
    else:
        if b % 2 == 0:
            print("The " + str(i+1) +"th digit is even")
            #print(b*10**i)
            n = n - b*10**i
            print(n)
        else:
            print("The " + str(i+1) +"th digit is odd")
            print(n)