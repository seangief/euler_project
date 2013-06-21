#generate a list of abundant numbers:
#	- find the divisors for a number, add them, if they are greater than the number, append them to a list
#	- I think I have code that does this

def main():
	abundant = [n for n in range(1,28124) if sum(divisors(n)) > 2*n]
	sums = set([i+j for i in abundant for j in abundant])
	answer = []
	for i in range(1,28124):
		if i not in sums	:
			answer.append(i)
	print sum(set(answer))

#this code is not mine. See:
# http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python

def divisors(n):
	return set(reduce(list.__add__, ([i, n/i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

if __name__ == "__main__":
	main()


