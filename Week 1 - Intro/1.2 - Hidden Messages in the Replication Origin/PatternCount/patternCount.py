
def patternCount(sequence, pattern):
    count = 0

    # Keeps sliding pattern through sequence, looking for matches
    for i in range(0, len(sequence) - len(pattern) + 1):
        if pattern in sequence[i:i+len(pattern)]:
            count += 1

    return count


def main():

    # Expecting two lines as the input
    with open('input.txt', 'r') as inputFile:
        dnaSequence = inputFile.readline().replace('\n', '')
        patternToCount = inputFile.readline().replace('\n', '')

    result = patternCount(dnaSequence, patternToCount)

	# Writes result to 'output.txt'
    with open('output.txt', 'w') as outputFile:
        outputFile.write(str(result))


if __name__ == '__main__':
    main()
