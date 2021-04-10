def getCommit(commit):
    return ''.join([i for i in commit if i not in ['0','?','+','!']])
