
# Function that finds the highest value on all keys on a dictionary
def maxDictValue(dict):

    # Check if dictionary is not empty
    if dict:
        values = dict.values()
        return max(values)
    else:
        raise ValueError("Dictionary is empty.")


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


# Function that finds the most frequent k-mers in a text
def betterFrequentWords(text, k):

    mostFrequentWords = []
    kmersDict = frequencyTable(text, k)
    maxVal = maxDictValue(kmersDict)

    for kmers in kmersDict.items():
        if kmers[1] == maxVal:
            mostFrequentWords.append(kmers[0])

    return mostFrequentWords


def main():

    with open('input.txt', 'r') as inputFile:
        text = inputFile.readline().replace('\n', '')
        k = int(inputFile.readline().replace('\n', ''))

    mostFrequent = betterFrequentWords(text, k)

    resultLength = len(mostFrequent)

    with open('output.txt', 'w') as outputFile:
        for count, results in enumerate(mostFrequent):
            outputFile.write(results)

            # Adds space to output, except on last element
            if count != resultLength - 1:
                outputFile.write(' ')


if __name__ == '__main__':
    main()
