def totalOfCombinations():
    comb = 8**(10 + 2*26)
    return comb

def numberChunksByChunkSize(chunkSize):
    comb = totalOfCombinations();
    numberChunks = comb / chunkSize
    return numberChunks
