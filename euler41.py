from isprime import *
import itertools

perm = list(itertools.permutations('1234567'))[::-1]
for s in perm:
	ans = int("".join(s))
	if isprime(ans):
		print ans
		break
