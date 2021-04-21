#! /usr/bin/env python3

def calcBonuses(bonuses, n):
    it = (x for x in bonuses)
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res
