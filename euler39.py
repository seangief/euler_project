import collections as c

def euler39():
	triplets = c.defaultdict(set)
	for i in range(1, 23):
		for j in range(1, i):
			count = 1
			o, a, h = i**2-j**2, 2*i*j, i**2+j**2
			s1, s2, s3 = 0, 0, 0
			while s1+s2+s3 < 1000:
				s1, s2, s3 = o*count, a*count, h*count
				if s1+s2+s3 < 1000:
					triplets[s1+s2+s3].add(frozenset([s1, s2, s3]))
				count += 1
	maxlen, maxperim = 0, 0
	for k, v in triplets.iteritems():
		if len(v) > maxlen:
			maxlen = len(v)
			maxperim = k
	print maxperim

if __name__ == "__main__":
	euler39()
