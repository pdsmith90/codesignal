#! /usr/bin/env python3

def pressureGauges(morning, evening):
    #return [[min([a,b]) for a,b in zip(morning,evening)],[max([a,b]) for a,b in zip(morning,evening)]]
    return list(zip(*[(min(x),max(x)) for x in zip(morning,evening)]))
