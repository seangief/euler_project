# P(win) = SUM (P(outcome) * P(opponent-has-less)) for all P

def euler205():
	pete_dist = dice_count(4,9)
	colin_dist = dice_count(6,6)

	ptotal, ctotal, ans = 4**9, 6**6, 0

	for outcome in xrange(1,37):
		ans += pete_dist[outcome]/float(ptotal) * sum(colin_dist[:outcome])/float(ctotal)

	print "Probability is %.7f" % ans

def dice_count(faces, number):
	matrix = [[0]*(faces*number+1) for row in xrange(number)]
	for num in xrange(1,faces+1):
		matrix[0][num] += 1
	for row in xrange(1, number):
		for item in xrange(len(matrix[row])):
			for dice in xrange(1,faces+1):
				if matrix[row-1][item] != 0:
					matrix[row][item+dice] += matrix[row-1][item]
	return matrix[-1]


if __name__ == "__main__":
	euler205()
