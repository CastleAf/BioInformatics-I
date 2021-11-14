
# Simple function that finds the indexes where the skewValue (G-C) is the lowest
def minSkew(sequence):

	skew = minVal = 0
	minVal = skew
	minIndex = [0]

	for index, nucleotide in enumerate(sequence):
		
		if nucleotide != 'A' and nucleotide != 'T':
			
			if nucleotide == 'G':
				skew += 1

			elif nucleotide == 'C':
				skew -= 1
			
			if skew <= minVal:
				if skew < minVal:
					minVal = skew
					minIndex.clear()

				minIndex.append(index + 1)
		
		else:
			if skew == minVal:
				minIndex.append(index + 1)

	return minIndex

def main():

	with open('input.txt', 'r') as inputFile:
		seq = inputFile.readline().replace('\n', '')

	result = minSkew(seq)
	resultLength = len(result)

	with open('output.txt', 'w') as outputFile:
		for count, results in enumerate(result):
			outputFile.write(str(results))

			# Adds space to output, except on last element
			if count != resultLength - 1:
				outputFile.write(' ')


if __name__ == '__main__':
	main()