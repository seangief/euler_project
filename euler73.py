import isprime as ip

def euler73(n):
	ans = 0
	for i in range(2,n):
		lbound = i/3 + 1
		rbound = (i+1)/2
		for digit in range(lbound, rbound):
			if ip.gcd(i,digit) == 1:
				ans+=1
	print ans

if __name__ == "__main__":
	euler73(12001)
