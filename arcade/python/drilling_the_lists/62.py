#! /usr/bin/env python3

def checkParticipants(participants):
    return [i[0] for i in list(filter(lambda x: x[1]<x[0], enumerate(participants) )) ]

#i heard you like one liners with lambdas and enumerate that also have an extra for loop in them

#returns list of indices where the value is less than the index
