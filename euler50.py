# Oh god this dataset thing is big.
# Wow.
# Most of the data is unused, I'm sure: the sum of the primes are waaaay too big to be useable.
# Dunno how to make them smaller, though.
# ansmatrix[first][lenght]

# ansmatrix[0][last] = sum(primes)
# ansmatrix[0][n] = ansmatrix[0][last] - ansmatrix[n][last]

# ansmatrix[n][last] = ansmatrix[0][last] - ansmatrix[0][n]

# ansmatrix[n][j] = ansmatrix[0][last] - (ansmatrix[0][n] + ansmatrix[j][last])

import isprime as ip

def euler50(limit):
	primes = list(ip.primes_sieve2((limit+1)/2))
	print sum(primes)
#	primeset = set(primes)
	size = len(primes)
	print size
#	ansmatrix = [[0] * size for x in range(size)]


#	ansmatrix[0][size-1] = sum(primes)
#	print ansmatrix[0][size-1]
#	ans = 0

#	for i in range(len(ansmatrix[0]))[::-1]:
#		ansmatrix[0][i-1] = ansmatrix[0][i] - primes[i]
#	
#	print len(ansmatrix), "x", len(ansmatrix[0])
#	
#	for i in range(len(ansmatrix[0])):
#		for j in range(1, len(ansmatrix)):
#			ansmatrix[j][i] = ansmatrix[0][i]-ansmatrix[j-1][j-1]
#			if ansmatrix[j][i] > limit:
#				break
#
#	print len(ansmatrix), "x", len(ansmatrix[0])

#	for i in range(len(ansmatrix)):
#		for j in range(len(ansmatrix[0])):
#			candidate = ansmatrix[i][j]
#			if candidate in primeset and candidate > ans:
#				ans = candidate
#			if candidate == 0:
#				break
	
#	print len(ansmatrix), "x ", len(ansmatrix[0])
#	print ans

if __name__ == "__main__":
	euler50(1000000)
