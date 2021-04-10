def transposeDictionary(scriptByExtension):
    return sorted(list([[x,y] for (y,x) in scriptByExtension.items()]))
