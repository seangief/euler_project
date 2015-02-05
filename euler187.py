def euler187():

	limit = 10**8
	ans = 0

	Primes = getprimes(limit/2)
	size = len(Primes)
	idx, prime_i = size-1, 0
	while prime_i <= idx:
		while (Primes[prime_i]*Primes[idx] >= limit):
			idx -= 1
		ans += idx-prime_i+1
		prime_i += 1
	print ans
		

def getprimes(limit):
	prime = []
	prime_mat = [False, False, True] + [True] *(limit-2)
	for i in xrange(2, limit+1):
		if prime_mat[i]:
			prime.append(i)
			for j in xrange(2*i, limit+1, i):
				prime_mat[j] = False
	return prime


if __name__ == "__main__":
	euler187()
