import math, fractions, collections as c

def isprime(n):
	if n < 2:
		return False
	elif n == 2 or n == 3:
		return True
	elif n%6 == 1 or n%6 == 5:
		for i in xrange(3,int(math.sqrt(n))+1, 2):
			if n%i == 0:
				return False
		return True
	else:
		return False

# This code I found at stackoverflow:
# http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
# I understand how it works though:
# it returns the set of all factors of n
# it uses a reduce() with the add function to append all lists of [p, q] where p*q = n

def allfacts(n):
	if n < 1: return [0]
	return set(reduce(list.__add__, 
		([i, n//i] for i in range(1, int(math.sqrt(n))+1) if n % i == 0)))


# Pollard rho algorithm. I wrote this.
def prfactor(n, key = lambda x : x**2+1):
	x, y, d = 2, 2, 1
	while d == 1:
		x = key(x) %n 
		y = key(key(y)) %n
		d = fractions.gcd(math.fabs(x-y), n)
	if d == n:
		return -1
	return d

# returns all prime factors of a number.
def primefact(n):
	return naieveFactor(n)

def primefactcomp(n):
	if n == 1:
		return 1
	else:
		r = [i for i in range(2,n) if gcd(i,n) == 0]
		return len(r)

def pollard_rho():
	test = [n]
	facts = []
	if n == 1: return [1]
	while test:
		t = test.pop()
		r = int(prfactor(t))

		# is possible that we have a false negative. Try two more pseudo-random functions
		# to be sure. Not sure if this is necessary in practice.
		if r == -1:
			r = int(prfactor(t, lambda x : x**2+4))
			if r == -1:
				r = int(prfactor(t, lambda x : x**2-4))

		#assume that, if r == -1 at this point, t is prime, or is 4
		if r == -1:
			if t == 4: facts.extend([2,2])
			else: facts.append(t)
		else:
			p, q = r, t/r
			test.extend([p, q])
	return facts

# I wrote this.
def divreduce(a,b):
	return (a/gcd(a,b), b/(gcd(a,b)))


# I wrote this.
def almostEq(a, b, epsilon = .000001):
	return math.fabs(a-b) < epsilon

# Calls the fractions library gcd function
def gcd(a, b):
	return fractions.gcd(a,b)

# Written for euler 69. Cool function:
def totient(n):
	if n == 1:
		return 1
	primef = dpfact(n)
	totient = n
	for prime in primef:
		totient /= prime
		totient *= prime-1
	return totient

# Returns distinct prime factors
def dpfact(n):
	return set(primefact(n))


# Prime sieve, implemented with yield, which I don't have much experience.
# Not mine, taken from:
# http://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python

def primes_sieve2(limit):
	a = [True] * limit                          # Initialize the primality list
	a[0] = a[1] = False

	for (i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in xrange(i*i, limit, i):     # Mark factors non-prime
 				a[n] = False


# for testing purposes:
def naieveFactor(n):
	primes, i = [], 2
	while n > 1:
		if n%i == 0:
			primes.append(i)
			n = n/i
		else:
			i+=1
	return primes


# http://stackoverflow.com/questions/1019040/how-many-numbers-below-n-are-coprimes-to-n
# slightly modifed
def totrange(n):
	totients = [1] * n
	totients[1] = totients[0]=0
	for i in range(2,n):
		if totients[i] == 1:
			for j in range(i,n, i):
				totients[j] *= i-1
				k = j/i
				while k%i == 0:
					totients[j] *= i
					k /= i
	return totients

'''
# original:
class Totient:
    def __init__(self, n):
  	      self.totients = [1 for i in range(n)]
        for i in range(2, n):
            if self.totients[i] == 1:
                for j in range(i, n, i):
                    self.totients[j] *= i - 1
                    k = j / i
                    while k % i == 0:
                        self.totients[j] *= i
                        k /= i
    def __call__(self, i):
        return self.totients[i]
if __name__ == '__main__':
    from itertools import imap
    totient = Totient(10000)
    print sum(imap(totient, range(10000)))
'''


def issquare(n):
	return int(math.sqrt(n))**2 == n

def spl_group(string):
    groups, buf = [], ''
    for letter in list(string):
        if buf and letter != buf[-1]:
            groups.append(buf)
            buf = letter
        else:
    		buf += letter
    else: 
        groups.append(buf)
    return groups
	


# populates a dictionary of partition numbers up to +including num
# pdict must include {0:1, 1:1}
def ppart(num, pdict):
	for value in range(2, num+1):
		partition, pcount, pent = 0, 1, 1
		while pent <= value:
			sign = (-1)**(pcount-1)
			partition += pdict[value - pent] * sign
			if pent+pcount <= value:
				partition += pdict[value - (pent+pcount)] * sign
			pcount += 1
			pent = (3*pcount**2 - pcount)/2
		pdict[value] = partition


# Check if (x1, y1), (x2, y2), (x3, y3) form a right triange.
def isRight((x1, y1), (x2, y2), (x3, y3)):
	v1, v2, v3 = (x1-x3, y1-y3), (x2-x3, y2-y3), (x2-x1, y2-y1)
	def dot((a1, b1), (a2, b2)):
		return a1*a2+b1*b2
	if dot(v1, v2) == 0 or dot(v2, v3) == 0 or dot(v1, v3) == 0:
		return True
	return False

def pell_eq(x1, y1, xk, yk, n):
	return (x1*xk)+(n*y1*yk), (x1*yk)+(y1*xk)

def neg_pell_eq(xn, yn):
	return (3*xn+4*yn, 2*xn+3*yn)


# Class represents rational numbers, supports +, -, /, * and comparison.
class rational():

	def __init__(self, num, denom):
		self.num = num
		self.denom = denom

	def __add__(self, other):
		return rational((other.num * self.denom) + (other.denom * self.num), 
		(other.denom)*(self.denom))

	def __repr__(self):
		return str(self.num)+'/'+str(self.denom)

 	def __float__(self):
		return float(self.num)/self.denom

	def isInteger(self):
		return (self.num % self.denom == 0 and self.denom != 0)

	def intVal(self):
		if self.isInteger():
			return self.num/self.denom
		return 0

	def __sub__(self, other):
		return rational(self.num*other.denom - self.denom*other.num,
		other.denom*self.denom)
	
	def __mul__(self, other):
		return rational(self.num*other.num, self.denom * other.denom)

	def __div__(self, other):
		return rational(other.denom * self.num,  other.num*self.denom)

	def __cmp__(self, other):
		return (self.num*other.denom - self.denom*other.num)


    #http://rosettacode.org/wiki/Modular_inverse#Python
def extend_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx-quotient*x, x
        y, lasty = lasty-quotient*y, y
    return lastremainder, lastx* (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

    #http://rosettacode.org/wiki/Modular_inverse#Python
def modinv(a, m):
    g, x, y = extend_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


'''
a dumb divreduce function I wrote:
nums = c.Counter(primefact(a))
	denoms = c.Counter(primefact(b))
	for factor in nums:
		if factor in denoms:
			common = min(nums[factor], denoms[factor])
			nums[factor] -= common
			denoms[factor] -= common
	return (reduce(int.__mul__, [k**v for k, v in nums.iteritems()]),
		reduce(int.__mul__, [k**v for k, v in denoms.iteritems()]))

If divreduce breaks anything (why?) replace it with this.
'''
