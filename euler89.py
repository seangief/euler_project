romanValues = [1000, 500, 100, 50, 10, 5, 1]
romanLetters = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

def getDecimal(groups, letters, values):
	roman = dict(zip(letters, values))
		
	decimal = []
	prev, total = 0, 0
	for group in groups[::-1]:
		curr = roman[group[0]]
		if prev > 0 and curr < prev:
			total -= curr * len(group)
		else:
			total += curr * len(group)
		prev = curr
	return total

def getRoman(decimal, letters, values):
	roman =  ''
	for idx in xrange(len(values)):
		length, decimal = divmod(decimal, values[idx])
		if length == 4 and letters[idx] != 'M': 
			roman += letters[idx] + letters[idx-1]
		else:
			roman += ''.join([letters[idx]] * length)
	# There's probably a 'clever' way to do this next bit, but I can't think of it.
	roman = roman.replace('VIV', 'IX')
	roman = roman.replace('LXL', 'XC')
	roman = roman.replace('DCD', 'CM')
	return roman
	
def euler89():
	total = 0
	romans = open("roman.txt").read().split('\n')
	for numeral in romans:
		minimal = getRoman(getDecimal(numeral, romanLetters, romanValues), romanLetters, romanValues)
		total += len(numeral) - len(minimal)
	print total


if __name__ == "__main__":
	euler89()

## VIV == IX
## something like this? if 
