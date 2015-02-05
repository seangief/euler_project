from isprime import totient
from math import factorial

# Use totrange!
# Ans is less than 23! (i.e. 25,852,016,738,884,976,640,000)
def euler243():
	bound, ans = float(15499)/94744, 0
	factorials = [factorial(x) for x in xrange(2,100)]
	for fact in factorials:
		if totient(fact)/float(fact-1) < bound:
			ans = fact
			break
	print ans

if __name__ == "__main__":
	euler243()
