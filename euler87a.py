# should be ~ 1,097,000
import math
from isprime import *

primes = []
#for i in range(1,50):
for i in range(1,7071):
	if isprime(i):
		primes.append(i)

sq = [i**2 for i in primes]
cub = [j**3 for j in primes] #81
quad = [k**4 for k in primes] #25

triplets = []

for x in quad:
	for y in cub:
		for z in sq:
			if x+y+z < 50000000:
				triplets.append(x+y+z)
			else:
				continue
print len(set(triplets))

