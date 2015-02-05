from collections import defaultdict

def euler86():
	S = set()
	for x in xrange(1, 301):
		for y in xrange(x+1, 301):
			a, b = y**2-x**2, 2*x*y
			for r in xrange(1,1000000/a):
				S.add((a*r, b*r))
				S.add((b*r, a*r))

	ans = defaultdict(int)

	for x, y in S:
		if y <= 2*x:
			for r in xrange(x, 10000):
				ans[r] += getRange(x, y)

	for x in xrange(1, 10000):
		if ans[x] > 1000000:
			print x
			break


def getRange(s1, s2s):
		if s2s <= s1:
			return s2s/2
		else:
			return s1-(s2s-1)/2

if __name__ == "__main__":
	euler86()																														


'''
t = []
for x, y in S:
	if x <= 100 and y <= 2*x:
			t.append((x,y))
'''

