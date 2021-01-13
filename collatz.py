def collatz(a):
    if ((a%2) == 0):    #number is even
        #a = int(a/2)
        a = a//2
        print(str(a))
        return(a)
    elif ((a%2) == 1):  #number is odd
        a = (a*3)+1
        print(str(a))
        return(a)
    else:
        print('Number is not a positive integer')
        return(1)

print('Enter a number:')

try:
    b = int(input())   #requests int input from user
    if b<0:
        print('Collatz sequence does not work on negative numbers')
    while (b > 1):
        b = collatz(b)
except ValueError:
    print('Error: argument is not an integer')