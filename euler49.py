import isprime as ip, itertools

def euler49():
	primes = [p for p in ip.primes_sieve2(10000) if p > 1000]
	ans = []

	for prime in primes:
		g = itertools.permutations(str(prime))
		perms = [int(''.join(permutation)) for permutation in g]
		test = []
		for num in perms:
			if num in primes:
				linear = (num - prime) + num
				if linear in primes and linear != num and linear in perms:
					ans.append(''.join([str(prime), str(num), str(linear)]))
					primes.remove(num)
	print ans
		

if __name__ == "__main__":
	euler49()
