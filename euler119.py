import isprime as ip, math as m

def euler119():
	count = 10
	ans = [1 for i in range(10)]
	start= 614656
	ibound = 1000000
	while count < 30:
		powers = sorted(list(powerset(start, ibound)))
		for power in powers:
			if isdigsumpower(power):
				count+=1
				start = power
				ans.append(power)
				if count == 30:
					break
				else:
					print power
		ibound*=10
	print "Final answer: ". ans[29]

def powerset(lowerbound, upperbound):
	powers = set()
	exptop = int(m.log(upperbound, 2)) + 1
	for exponent in range(2, exptop):
		baserange = int(upperbound ** (float(1)/exponent))
		for i in range(2, baserange+1):
			power = i**exponent
			if power > lowerbound and power < upperbound:
				powers.add(power)
	return powers

def isdigsumpower(num):
	digsum = sum(int(i) for i in str(num))
	try:
		return num == digsum**int(m.log(num, digsum))
	except:
		return False

if __name__ == "__main__":
	euler119()


'''

1679616
17210368
34012224
52521875
60466176
612220032
8303765625
10460353203
24794911296
27512614111
52523350144
68719476736
271818611107
2207984167552
20047612231936
72301961339136
248155780267521

'''
