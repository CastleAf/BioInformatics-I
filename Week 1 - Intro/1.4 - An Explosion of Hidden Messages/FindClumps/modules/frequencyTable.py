# Function that counts the frequency of all the k-mers in a text
def frequencyTable(text, k):

    freqDict = {}
    textLength = len(text)

    for i in range(0, textLength - k):
        pattern = text[i:i+k]

        if pattern not in freqDict:
            freqDict[pattern] = 1
        else:
            freqDict[pattern] += 1

    return freqDict