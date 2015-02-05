import isprime as ip
def euler51():
	ansdict = dict()
	found = False
	winner = ''
	for candidate in xrange(10001, 100000000, 2):
		if ip.isprime(candidate):
			digits = str(candidate)
			for digit in set(digits):
				pattern = digits.replace(digit, '*')
				if pattern not in ansdict:
					ansdict[pattern] = [0,[]]
					for otherdigit in range(10):
						newcandidate = int(pattern.replace('*', str(otherdigit)))
						if ip.isprime(newcandidate) and len(str(newcandidate)) == len(str(candidate)):
							ansdict[pattern][0] += 1
							ansdict[pattern][1].append(int(newcandidate))
							if ansdict[pattern][0] == 8:
								winner = pattern
								found = True
		if found == True:
			break
	print ansdict[winner][1]
	print min(ansdict[winner][1])


if __name__ == "__main__":
	euler51()

