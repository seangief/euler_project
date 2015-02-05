from math import sqrt

def euler206():
	base = '1_2_3_4_5_6_7_8_9_0'
	firstpart = base[:8]
	lastpart = base[8:]
	ans, done, number = 0, False, 0

	while number < 10000 and not done:
		digits = list('%04d' % number)
		newnum = list(firstpart)
		for index, digit in enumerate(digits):
			newnum[2*index+1] = digit
		minimum = int(sqrt(int(''.join(newnum) + lastpart.replace('_','0'))))
		maximum = int(sqrt(int(''.join(newnum) + lastpart.replace('_','9')))) + 1
		test = minimum
		while test < maximum:
			if isanswer(str(test**2), base):
				ans = test
				done = True 
			test+=1
		number += 1

	print ans

def isanswer(testnum, base):
	testnum = list(testnum)
	for index in range(len(testnum)):
		if index %2 == 1: testnum[index] = '_'
	return (''.join(testnum) == base)


if __name__ == "__main__":
	euler206()
