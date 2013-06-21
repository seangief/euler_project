def euler23():
	import Euler12a
	abundant = getAbundant()
	return

def getAbundant():
	bound = 28123
	abundant = []

	for i in rage(bound):
		if (2*i) < sum(factors(i)):
			abundant.append(i)
	return abundant


## not my code. Code by agf from stackoverflow. I understand this but don't
## know much about lists. 
## http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n/i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))



k = set(range(1,28124))
bound = max(k)
n = 
while (n < bound):
	

# Use set functions!:
#http://docs.python.org/2/library/stdtypes.html#set

