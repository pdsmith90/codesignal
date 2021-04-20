#! /usr/bin/env python3

def fibonacciList(n):
    return [[0] * x for x in functools.reduce(lambda x,y: x+[x[-1]+x[-2]] ,range(2,n),[0,1])]
