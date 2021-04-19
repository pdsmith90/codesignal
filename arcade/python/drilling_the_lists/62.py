#! /usr/bin/env python3

def checkParticipants(participants):
    return [i[0] for i in list(filter(lambda x: x[1]<x[0], enumerate(participants) )) ]
