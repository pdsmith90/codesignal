from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda x: res[x].rotate(-x),range(len(res))), 0)
    return [list(d) for d in res]
