import isprime as ip, collections as c

def euler95():
	pathlength, pathnum = 0, 0
	nums = c.defaultdict(int)
	for i in range(0, 1000000):
		test = amicable(i, nums)
		if test > pathlength:
			pathlength = test
			pathnum = i
	print pathnum


# don't understand why this isn't working. amicable(7524, d) returns -1 when I call it via
# commandline, but somehow during the program it gets set to something else. The answer is clearly
# the chain discovered by 7524, but 7524 itself is not part of the chain.
def amicable(original, nums):
	chainstart = 0
	n = original
	length = 0
	path = []
	done = False

	while not done:
		if nums[n] != 0:
			length = nums[n]
			done = True
		else:
			if n > 1000000 or n == 0:
				length = -1
				done = True
			elif n in path:
				chainstart = path.index(n)
				length = len(path[chainstart:])
				done = True
			else:
				path.append(n)
				n = sum(ip.allfacts(n))-n
	for inchain in path[chainstart:]: 
		nums[inchain] = length
	for outchain in path[:chainstart]:
		length = -1
		nums[outchain] = length
	return length

if __name__ == "__main__":
	euler95()


