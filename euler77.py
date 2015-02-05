from collections import Counter
import isprime as ip

def euler77():
	def polymult(dic1, dic2, limit):
		d = Counter()
		values1, values2 = dic1.keys(), dic2.keys()
		for monomial1 in values1:
			for monomial2 in values2:
				value = monomial1 + monomial2
				if value <= limit:
					d[value] += dic1[monomial1] * dic2[monomial2]
		return d

	def genfunct(number, limit):
		return Counter([number * a for a in xrange(limit+1) if number*a <= limit])

	limit, ans = 100, 1000
	primes = ip.primes_sieve2(limit)
	partitions = polymult(genfunct(primes.next(), limit), genfunct(primes.next(), limit), limit)
	for prime in primes:
		partitions = polymult(partitions, genfunct(prime, limit), limit)

	for key, value in partitions.iteritems():
		if value > 5000 and key < ans:
			ans = key
	print ans

if __name__ == "__main__":
	euler77()
