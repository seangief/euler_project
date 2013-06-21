import string, math

def euler74():
	tfact = [math.factorial(i) for i in range(0,10)]
	facts  = dict(zip(string.digits, tfact))
	chainlength = dict()
	ans = set()

	for i in range(1, 1000000):
		num = str(i)
		length = 0
		path = []
		done = False
		while not done:
		        if num in chainlength:
		                length += chainlength[num]
		                done = True
		        else:
			        next = str(sum([facts[d] for d in num]))
		                length += 1
		                path.append(num)
		                num = next
		                if next in path:
		                        done = True
		for s in path:
			chainlength[s] = length
			if length == 60:
				ans.add(s)
			length -= 1
	print len(ans)

if __name__ == "__main__":
	euler74()
