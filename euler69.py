import isprime as ip

def euler69():
	maximum = 0.0
	ans = 0
	for i in range(1, 1000000):
		if float(i)/totient(i) > maximum:
			maximum = float(i)/totient(i)
			ans = i
	print ans

def totient(n):
	if n == 1:
		return 1
	primef = ip.dpfact(n)
	totient = n
	for prime in primef:
		totient /= prime
		totient *= prime-1
	return totient

if __name__ == "__main__":
	euler69()

