import isprime as pr

def euler37():
	ans = []
	starting = 10
	while len(ans) < 11:
		primes = [i for i in range(starting, starting+10000) if pr.isprime(i)]
		starting += 10000
		for prime in primes:
			primestr = (str(prime), str(prime))
			trunc = True
			while len(primestr[0]) > 1:
				primestr = (primestr[0][1:], primestr[1][:len(primestr[1])-1])
				if not (pr.isprime(int(primestr[0])) and pr.isprime(int(primestr[1]))):
					trunc = False
					break
			if trunc:
				ans.append(prime)
	print ans
	print sum(ans)

if __name__ == "__main__":
	euler37()
