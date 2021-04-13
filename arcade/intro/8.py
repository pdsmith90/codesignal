#!/bin/python3

def matrixElementsSum(matrix):
    spooked=[]
    roomSum=0
    for i in enumerate(matrix):
        rooms = [x for i, x in enumerate(i[1]) if i not in spooked]
        roomSum+=sum(rooms)
        for j in enumerate(i[1]):
            if j[1]==0: spooked.append(j[0]) 
    return roomSum
