#! /usr/bin/env python3


def mathPractice(numbers):
    return functools.reduce(lambda s, x: s*x[0]+x[1], list(zip((numbers+[0])[0::2],(numbers+[0])[1::2])),1)



#def myFun(sum1,next1):
#
#    if count % 2 == 1:
#        count+=1
#        return sum1 * next1
#        
#    else:
#        count+=1
#        return sum1 + next1
        
