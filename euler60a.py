def euler60():
	from isprime import primes_sieve2
	from itertools import combinations

	primes = list(primes_sieve2(10000))
	edges = {}
	for index, prime1 in enumerate(primes[:-1]):
		edges[prime1] = set()
		for prime2 in primes[index+1:]:
			if testprime(prime1, prime2):
				edges[prime1].add(prime2)

	ans, ansset = 1000000, []

	for vertex, neighbors in edges.iteritems():
		for neighbor in neighbors:
			try:
				shared = neighbors & edges[neighbor]
			except KeyError:
				shared = set()
			if len(shared) >= 3:
				cliques = combinations(shared, 3)
				for clique in cliques:
					clique = list(clique)
					if testclique(clique, edges):
						testset = [vertex, neighbor]
						testset.extend(clique)
						if sum(testset) < ans:
							ansset = testset
							ans = sum(testset)
	print ans


def testprime(num1, num2):
	from isprime import isprime
	return isprime(int(str(num1) + str(num2))) and isprime(int(str(num2) + str(num1)))


def testclique(clique, edges):
	clique.sort()
	isclique = True
	for index, item1 in enumerate(clique[:-1]):
		for item2 in clique[index+1:]:
			isclique = isclique and (item2 in edges[item1])
	return isclique

if __name__ == "__main__":
	euler60()

