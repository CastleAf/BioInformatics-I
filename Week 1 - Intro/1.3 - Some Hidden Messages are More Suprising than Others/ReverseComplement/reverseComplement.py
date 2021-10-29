
def reverseComplement(dnaSeq):

	adenine = 'A'
	cytosine = 'C'
	guanine = 'G'
	thymine = 'T'
	reverse = []

	for nucleotide in reversed(dnaSeq):

		if nucleotide == adenine:
			reverse.append(thymine)
		elif nucleotide == cytosine:
			reverse.append(guanine)
		elif nucleotide == guanine:
			reverse.append(cytosine)
		elif nucleotide == thymine:
			reverse.append(adenine)
		else:
			raise ValueError('Unknown dna nucleotide found.')

	return ''.join(reverse)


def main():

	with open('input.txt', 'r') as inputFile:
		dna = inputFile.readline().replace('\n', '')

	reverse = reverseComplement(dna)

	with open('output.txt', 'w') as outputFile:
		outputFile.write(reverse)


if __name__ == '__main__':
	main()