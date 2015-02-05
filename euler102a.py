# see http://www.blackpawn.com/texts/pointinpoly/

def cross((ax,ay), (bx,by)):
	az, bz = 0, 0
	xnew = (ay*bz)-(by*az)
	ynew = -1 * ((ax*bz)-(bx*az))
	znew = (ax*by)-(bx*ay)
	return (xnew, ynew, znew)

def dot((ax, ay, az), (bx, by, bz)):
	return (ax*bx)+(ay*by)+(az*bz)
 
def sameside((p1x, p1y), (p2x, p2y), (ax, ay), (bx, by)):
	cp1 = cross((bx-ax, by-ay), (p1x-ax, p1y-ay))
	cp2 = cross((bx-ax, by-ay), (p2x-ax, p2y-ay))
	if dot(cp1, cp2) >= 0: return True
	else: return False

def pointInTriangle(p, a, b, c):
	if sameside(p, a, b, c) and sameside(p, b, a, c) and sameside(p, c, a, b): return True
	else: return False


def euler102():
	points = open("triangles.txt").read().split('\n')[:1000]
	triangles = []
	for line in points:
		coords, triangle = line.split(','), []
		for idx in xrange(0, len(coords), 2):
			triangle.append( (int(coords[idx]), int(coords[idx+1])) )
		triangles.append(triangle)

	ans = 0
	for a, b, c in triangles:
		if pointInTriangle((0,0), a, b, c): ans += 1

	print ans

if __name__ == '__main__':
	euler102()
