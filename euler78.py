# populates a diction of partition numbers up to +including num
# estimated no. of computations: sum( floor(1+ sqrt(24*n+1))/2) ) for 0 < n <= 100000
def ppart(num, pdict):
	for value in range(2, num+1):
		partition, pcount, pent = 0, 1, 1
		while pent <= value:
			sign = (-1)**(pcount-1)
			partition += pdict[value - pent] * sign
			if pent+pcount <= value:
				partition += (pdict[value - (pent+pcount)] * sign)
			pcount += 1
			pent = (3*pcount**2 - pcount)/2
		pdict[value] = partition % 1000000

def euler78():
	ans, pdict = 0, {0:1, 1:1}
	ppart(100000, pdict)
	
	#by Ramanujan's congruence, P(5k+4) == 0 (mod 5)
	for attempt in [5*i+4 for i in xrange(1, 20000)]:
		if pdict[attempt] == 0:
			ans = attempt
			break
	print ans, pdict[ans]

if __name__ == "__main__":
	euler78()
