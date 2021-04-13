
from itertools import combinations

def crazyball(players, k):
    return sorted(combinations(sorted(players),k))
