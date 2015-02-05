# It is possible that there is a divide & conquer recursive algorithm for this:
# e(2) = e1+f(e(1)), etc. I don't know.
# Here's my attempt using linear algebra.
def euler91(limit):
	count = 0
	points = createPoints(limit)
	while points:
		(x1, y1) = points.pop()
		for (x2, y2) in points:
			if isRight((x1, y1), (x2, y2), (0,0)):
				count += 1
	print count

def isRight((x1, y1), (x2, y2), (x3, y3)):
	v1, v2, v3 = (x1-x3, y1-y3), (x2-x3, y2-y3), (x2-x1, y2-y1)
	def dot((a1, b1), (a2, b2)):
		return a1*a2+b1*b2
	if dot(v1, v2) == 0 or dot(v2, v3) == 0 or dot(v1, v3) == 0:
		return True
	return False

def createPoints(limit):
	points = []
	for x in xrange(limit+1):
		for y in (xrange(limit+1)):
			if (x, y) == (0, 0): continue
			else: points.append((x, y))
	return points

if __name__ == "__main__":
	euler91(50)

