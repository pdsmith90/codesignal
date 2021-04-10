def wordsRecognition(word1, word2):
    def getIdentifier(w1, w2):
        return ''.join(sorted(list(set(filter(lambda x: x not in w2, w1)))))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]
