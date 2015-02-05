import isprime as ip

def euler94():
	ans = 0
	for num in xrange(3, 166666667):
		test = 3*num**2 + 4*num + 1
		perimeter = 6*num+2
		if perimeter < 1000000000:
			if ip.issquare(test):
				ans += perimeter

		test = 3*num**2 - 4*num + 1
		perimeter = 6*num-2
		if perimeter < 1000000000:
			if ip.issquare(test):
				ans += perimeter
	print ans

if __name__ == "__main__":
	euler94()
