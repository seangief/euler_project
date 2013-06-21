import itertools as it
import isprime as pr


# except even if this ran quickly enough, it would never produce a combo like (5, 17, 173)
# maybe it should go along until it finds a pair of primes whose cat is also prime, then
# go to the next prime, then the next, testing cat combos until it finds the smallest 
# every prime bigger than 5 ends in 1, 3, 7 or 9

def euler60():
	base = 7
	found = False
	answer = []
	while not found:
		primeset = [str(i) for i in range(base, base+25) if pr.isprime(i)]
		combs = it.combinations(primeset, 5)
		
		for combo in combs:
			perms = it.permutations(combo, 2)
			ppairset = True
			for perm in perms:
				if not pr.isprime(int("".join(perm))):
					ppairset = False
					break
			if ppairset:
				found = True
				answer.append(list(combo))
				break
		base += 25
	print min([sum(ppair) for ppair in answer])

if __name__ == "__main__":
	euler60()
