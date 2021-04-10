def firstDuplicate(a):
    aUnique = set()
    aUnique.add(-1)
    a.append(-1)
    for aa in a:
        if aa not in aUnique:
            aUnique.add(aa)
        else:
            return aa
            break
