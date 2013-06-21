import isprime as ip

def euler47():
	i, numfacts = 1, dict()
	solved = False
	while not solved:
		i += 1
		j = len(set(ip.primefact(i)))
		numfacts[i] = j
		if j == 4:
			if numfacts[i-1] == 4 and numfacts[i-2] == 4 and numfacts[i-3] == 4:
				solved = True
	print "Answer: ", i-3

if __name__ == "__main__":
	euler47()
