def wordPower(word):
    num = {y: int(ord(y)) - 96 for x,y in enumerate(word)}
    return sum([num[ch] for ch in word])
