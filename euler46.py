import isprime as ip, math as m

def euler46():

	def comp_sieve(limit):
		a = [True] * limit
		a[0] = a[1] = False

		for (i, isprime) in enumerate(a):
			if isprime:
				for n in xrange(i*i, limit, i):
	 				a[n] = False
			else:
				if i%2 == 1:
		 			yield i


	g = comp_sieve(1000000)
	composites = list(comp_sieve(1000000))	
	done = False

	g.next() # get rid of "1"


	while not done:
		count = g.next()
		sqt = int(m.sqrt(count/2))
		while sqt > 0:
			primec = count - 2*(sqt**2)
			if primec in composites: 
				sqt-=1
			else:
				break
		if sqt == 0:
			done = True
#		else:
#			print "%d = 2*(%d**2)+%d" % (count, sqt, primec)
	print count


if __name__ == "__main__":
	euler46()

