# Efficient way to generate all right triangles with perimeter <= p
# To find the maximum bound for a, remember, 2a**2+2a <= p
import collections as c

def euler75():
	triplets = c.defaultdict(set)
	for i in range(1, 866):
		for j in range(1, i):
			count = 1
			o, a, h = i**2-j**2, 2*i*j, i**2+j**2
			s1, s2, s3 = 0, 0, 0
			while s1+s2+s3 < 1500000:
				s1, s2, s3 = o*count, a*count, h*count
				if s1+s2+s3 < 1500000:
					triplets[s1+s2+s3].add(frozenset([s1, s2, s3]))
				count += 1
	ans = 0
	for k, v in triplets.iteritems():
		if len(v) == 1:
			ans+=1
	print ans

if __name__ == "__main__":
	euler75()
