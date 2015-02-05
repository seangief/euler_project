from math import sqrt

def euler173():
	limit, count = 1000001, 0

	for i in xrange(3, limit/4+2):
		count += find_lamina(i, limit)
	print "The number of lamina is %d" % count

def find_lamina(side, limit):
	area, min_hole, max_hole = side**2, 1 + ((side + 1) % 2), side-1
	if area > limit:
		if side % 2 == 0:
			min_hole = even(side, limit)
		else:
			min_hole = odd(side, limit)
	return (1 + max_hole - min_hole)/2

def odd(side, limit):
	return 2 *(int(4 + sqrt(16-16*(1-side**2+limit)))/8) +1

def even(side, limit):
	return int(sqrt(side**2-limit)/2) *2+2


if __name__ == "__main__":
	euler173()

