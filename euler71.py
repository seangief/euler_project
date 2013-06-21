import isprime as ip

def euler71(n):
	smallest = 1
	ans = 0
	testpt = float(3)/7
	for i in range(2,n):
		nearest = (3*i)/7
		if nearest == 0:
			nearest = 1
		fract = nearest/float(i)
		if ip.gcd(nearest, i) == 1:
			if testpt-fract < smallest and testpt-fract > 0:
				ans = nearest
				smallest = testpt-fract
	print ans

if __name__ == "__main__":
	euler71(1000000)
