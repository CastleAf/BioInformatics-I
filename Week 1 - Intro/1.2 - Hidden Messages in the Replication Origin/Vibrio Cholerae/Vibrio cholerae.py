# Simple prog to verify the origin of replication in Vibrio cholerae's genome


def main():

	with open('Vibrio cholerae.txt', 'r') as genomeFile:
		wholeGenome = genomeFile.read().replace('\n', '').upper()

	with open('Vibrio cholerae ori.txt', 'r') as oriFile:
		ori = oriFile.read().replace('\n', '').upper()

	if ori in wholeGenome:
		print('Ori found on genome!')
	else:
		print('Ori not found.')


if __name__ == '__main__':
	main()
