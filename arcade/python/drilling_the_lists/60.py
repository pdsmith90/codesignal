#! /usr/bin/env python3

#def prefSum(a):
#    return [sum(a[:i]) for i in range(1,len(a)+1)]

def prefSum(a):
    return functools.reduce(lambda x,y: x + [x[-1]+y],a,[0])[1:]
