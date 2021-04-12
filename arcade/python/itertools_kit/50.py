from itertools import count, takewhile

def floatRange(start, stop, step):
    gen = takewhile(lambda x: x<stop, (start + i * step for i in count()))
    return list(gen)
