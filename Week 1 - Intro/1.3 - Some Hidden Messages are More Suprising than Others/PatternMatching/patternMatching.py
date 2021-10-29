
def patternMatching(pattern, sequence):
    indexes = []

    # Keeps sliding pattern through sequence, saving the index when finding matches
    for i in range(0, len(sequence) - len(pattern) + 1):
        if pattern in sequence[i:i+len(pattern)]:
            indexes.append(i)

    return indexes


def main():

    with open('input.txt', 'r') as inputFile:
        pattern = inputFile.readline().replace('\n', '')
        genome = inputFile.readline().replace('\n', '')

    indexPositions = patternMatching(pattern, genome)
    resultLength = len(indexPositions)

    with open('output.txt', 'w') as outputFile:
        for count, index in enumerate(indexPositions):
            outputFile.write(str(index))

            # Adds space to output, except on last element
            if count != resultLength - 1:
                outputFile.write(' ')


if __name__ == '__main__':
    main()
