from isprime import *

counter, twopower, total, primes, side = 49, 8, 13, 8, 7
#primes = [3, 5, 7, 13, 17, 31, 37]

while (float(primes)/total > .1):
	for i in range(4):
		counter+=twopower
		if isprime(counter):
			primes+=1
		total+=1
	twopower +=2
	side +=2
print side

