
# Simple function that evaluates G - C nucleotides across a sequence 
def skew(sequence):

	skewVals = [0]

	for index, nucleotide in enumerate(sequence):
		if nucleotide == 'G':
			skewVals.append(skewVals[index] + 1)

		elif nucleotide == 'C':
			skewVals.append(skewVals[index] - 1)
		
		else:
			skewVals.append(skewVals[index])

	return skewVals

def main():

	with open('input.txt', 'r') as inputFile:
		seq = inputFile.readline().replace('\n', '')

	result = skew(seq)
	resultLength = len(result)

	with open('output.txt', 'w') as outputFile:
		for count, results in enumerate(result):
			outputFile.write(str(results))

			# Adds space to output, except on last element
			if count != resultLength - 1:
				outputFile.write(' ')


if __name__ == '__main__':
	main()