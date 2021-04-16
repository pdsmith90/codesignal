#! /usr/bin/env python3

def prefSum(a):
    return [sum(a[:i]) for i in range(1,len(a)+1)]
