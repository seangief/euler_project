def euler66():
	ans, ansmax = 0, 0
	for num in xrange(2, 1001):
		try:
			x, y = getApprox(continuedroot(num))
#			print x, y
			if x > ansmax:
				ans, ansmax = num, x
		except StandardError:
			continue
	print ans

def continuedroot(number):
	from math import sqrt
	m, d, a, continued, Done = 0, 1, int(sqrt(number)), [], False
	a0 = a
	if a0**2 == number:
		raise StandardError("Cannot find a continued fraction for the root of a perfect square")
	else:
		while not Done:
			m = d*a-m
			d = (number - m**2)/d
			a = (a0+m)/d
			continued.append(a)
			if a == 2*a0:
				Done = True
		return a0, continued

def getApprox(infroot):
	integer, fract = infroot
	if len(fract) == 1:
		num, denom = 1, fract.pop()
	else:
		fract = fract[:-1] # fract should be a palindrome
		num, denom = 1, fract.pop()
		while fract:
			denom, num = denom*fract.pop() + num, denom
	return (integer*denom+num, denom)

