from math import sqrt

def euler139(max_perimeter):
	bound = int((sqrt(2+2*max_perimeter)-1)/4)+1
	ans = 0
	for i in range(1, bound):
		for j in range(1, i):
			count = 1
			o, a, h = i**2-j**2, 2*i*j, i**2+j**2
			s1, s2, s3 = o, a, h
			if s3 % abs(s1-s2) == 0:
				while s1+s2+s3 < max_perimeter:
					s1, s2, s3 = o*count, a*count, h*count
					ans += 1
					count += 1
	print ans

if __name__ == "__main__":
	euler139(10**8)
