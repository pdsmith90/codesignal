def permutationCipher(password, key):
    table = password.maketrans(string.ascii_lowercase, key)
    return password.translate(table)
