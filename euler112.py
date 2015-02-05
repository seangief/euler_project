def euler112():
	nonbouncyarray = [True] * 100 + [False] * (10000000 - 100)
	for number in xrange(100,10000000):
		stem, branch = divmod(number, 10)
		nonbouncyarray[number] = nonbouncyarray[stem] and issequence(stem, branch)
	counter, bouncy = 99, 0
	while (99*counter) != (100 * bouncy):
		counter+=1
		if not nonbouncyarray[counter]:
			bouncy += 1
	print counter

def issequence(number, candidate):
	from math import log
	magnitude = int(log(number)/log(10))
	last = number % 10
	first = number/10**magnitude
	return ((first <= last) and (last <= candidate)) or ((last <= first) and (candidate <= last))

if __name__ == "__main__":
	euler112()
