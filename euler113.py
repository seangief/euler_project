def euler113(limit):
	oldBouncy, currBouncy, maxdigits = [1] * 10, [], 2
	if limit < 2:
		currBouncy = oldBouncy
	while maxdigits <= limit:
		currBouncy = [maxdigits] + [0] * 9
		for startdigit in xrange(1,10):
			currBouncy[startdigit] = oldBouncy[startdigit] + currBouncy[startdigit-1]
		oldBouncy = currBouncy
		maxdigits += 1
	print sum(currBouncy[1:]) + sum(currBouncy[:9]) - 9*limit

if __name__ == "__main__":
	euler113(100)
