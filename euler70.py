import isprime as ip, sys, collections as c

def euler70():
	totvals = ip.totrange(10000000)
	ans = 0
	ansrat = sys.maxint
	for i in range(2, len(totvals)):
		totient = totvals[i]
		palindrome = True
		if len(str(i)) == len(str(totient)):
			a, b = c.Counter(str(i)), c.Counter(str(totient))
			for val in a:
				if a[val] != b[val]:
					palindrome = False
					break
		if palindrome:
			if float(i)/totient < ansrat:
				ans, ansrat = i, float(i)/totient
	print ans

if __name__ == "__main__":
	euler70()
