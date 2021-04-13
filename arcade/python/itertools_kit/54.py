from itertools import product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted(filter(lambda x: int(x)%d==0, [createNumber(x) for x in product(digits, repeat=k)]))
