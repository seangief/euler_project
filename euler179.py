
def euler179():
	limit = 10**7+1
	divs = [0, 1] + [2]*(limit-1)
	ans = 0

	for num in xrange(2, limit):
		for j in xrange(num, limit, num):
			divs[j] += 1
		if divs[num] == divs[num-1]:
			ans += 1

	print ans

if __name__ == "__main__":
	euler179()

