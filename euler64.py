def euler64():
	ans = 0
	for number in xrange(1, 10001):
		if len(continuedroot(number)) % 2 == 1:
			ans += 1
	print ans

# totally not my genius, see http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
def continuedroot(number):
	from math import sqrt
	m, d, a, continued, Done = 0, 1, int(sqrt(number)), [], False
	a0 = a
	if a0**2 == number:
		return [0,0]
	else:
		while not Done:
			m = d*a-m
			d = (number - m**2)/d
			a = (a0+m)/d
			continued.append(a)
			if a == 2*a0:
				Done = True
		return continued

if __name__ == "__main__":
	euler64()
