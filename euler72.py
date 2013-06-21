import isprime as ip

def euler72():
	bound = 11+1
	ans = 0
	tot = dict()
	tot[4] = 2
	primes = [i for i in range(bound) if ip.isprime(i)]
	for prime in primes:
		tot[prime] = prime-1
	for i in range(2, bound):
		ans += totient(i, tot)
	print ans
	return tot

# Euler's totient uses each unique prime once. This currently runs all prime factors. 
# There might be another problem too...
# Output:
# num  e72    correct
# 2	1	1
# 3	2	2
# 4	2	2
# 5	4	4
# 6	2	2
# 7	6	6
# 8	2	4
# 9	4	6
# 10	4	4
# So maybe numbers with squares? 8 = 2**2 *2, 9 = 3**2

def totient(n, tot):
	if n not in tot:
		factor = ip.prfactor(n)
		if factor == -1:
			factor = int(ip.prfactor(n, lambda x : x**2+4))
			if factor == -1:
				factor = int(ip.prfactor(n, lambda x : x**2-4))
		if factor == -1:
			tot[n] = n-1
		else:
			tot[n] = totient(factor, tot) * totient(n/factor, tot)
	return tot[n]


if __name__ == "__main__":
	euler72()
