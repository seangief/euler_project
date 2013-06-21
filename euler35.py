import isprime as pr

def euler35():
	ans = []
	primeset = [i for i in range(2,1000000) if pr.isprime(i)]
	for i in primeset:
		if i not in ans:
			prime = str(i)
			circprimes = set()
			iscirc = True
			for j in range(0, len(prime)):
				circprime = int(prime[j:] + prime[:j])
				circprimes.add(circprime)
				if not pr.isprime(circprime):
					iscirc = False
					break
			if iscirc:
				ans.extend(circprimes)
	print ans
	print len(ans)

if __name__ == "__main__":
	euler35()
