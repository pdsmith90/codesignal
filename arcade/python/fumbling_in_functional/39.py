from fractions import gcd

def leastCommonDenominator(denominators):
    return functools.reduce(lambda x,y : x*y/gcd(x,y), denominators)
