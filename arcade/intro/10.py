#!/usr/bin/env python3

def commonCharacterCount(s1, s2):
    count=0
    s2=list(s2)
    for x in s1:
        if x in s2: 
            s2.remove(x)
            count+=1
    
    return count
