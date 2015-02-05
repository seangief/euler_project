def countRect(gridLength, gridWidth):
	return (gridLength**2+gridLength)/2 * (gridWidth**2+gridWidth)/2

def findNearest(gridLength):
	from math import sqrt
	g = (gridLength**2+gridLength)/2
	c = (2*2000000) / g
	return int((-1 + sqrt(1+4*c))/2)

def euler85():
	diff, ans = 1000000, (0,0)
	for xnum in xrange(1, 2000):
		nearest = findNearest(xnum)
		cr1, cr2 = countRect(xnum, nearest), countRect(xnum, nearest+1)
		if abs(2000000 - cr1) < diff:
			diff = abs(2000000-cr1)
			ans = (xnum, nearest)
		if abs(2000000 - cr2) < diff:
			diff = abs(2000000-cr2)
			ans = (xnum, nearest+1)
	print ans[0]*ans[1]

