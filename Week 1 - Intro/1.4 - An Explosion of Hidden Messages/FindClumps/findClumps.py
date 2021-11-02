from modules.frequencyTable import frequencyTable

def findClumps(genome, kmerL, windowL, tVal):

	clumps = []
	n = len(genome)

	for i in range(0, n - windowL):
		window = genome[i:i + windowL]
		kmersDict = frequencyTable(window, kmerL)

		for kmers in kmersDict.items():
			if kmers[1] >= tVal:
				clumps.append(kmers[0])

	# Removes duplicates as dictionaries can't have duplicates
	clumps = list(dict.fromkeys(clumps))

	return clumps


def main():

	with open('input.txt', 'r') as inputFile:
		text = inputFile.readline().replace('\n', '')
		vals = inputFile.readline().replace('\n', '').split()

	kmerLength = int(vals[0])
	windowLength = int(vals[1])
	tVal = int(vals[2])

	obtainedClumps = findClumps(text, kmerLength, windowLength, tVal)
	resultLength = len(obtainedClumps)

	with open('output.txt', 'w') as outputFile:
		for count, results in enumerate(obtainedClumps):
			outputFile.write(results)

			# Adds space to output, except on last element
			if count != resultLength - 1:
				outputFile.write(' ')


if __name__ == '__main__':
	main()
