def allLongestStrings(inputArray):
    maxLen=len(max(inputArray,key=len))
    maxArray=[x for x in inputArray if len(x)==maxLen]
    return maxArray
