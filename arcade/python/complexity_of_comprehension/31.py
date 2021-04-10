def constructShell(n):
    return [[0]*i for i in range(1,n+1,)] + [[0]*(i) for i in range(n-1,0,-1)]
