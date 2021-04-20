#! /usr/bin/env python3

def primesSum(a, b):
    return sum( filter(isPrime, range(a,b+1)) )



#sick of illegible one liners so heres a function to find primes
def isPrime(a):
    # returns true/false to be used with filter
    
    #first 3 numbers:
    if (a <= 1):
        return False
    elif (a <= 3):
        return True

    #check if divisible by 2 or 3:
    elif (a % 2 == 0 or a % 3 == 0):
        return False
    
    #loop
    i = 5
    while(i * i <= a):
        if (a % i == 0 or a % (i + 2) == 0):
            return False
        i = i + 6
 
    return True
