from itertools import permutations

def rockPaperScissors(players):
    return sorted(permutations(players,2))
