#import euler65 as e
#	

def euler65():
	k = edenom(100)
	f = fractiter(2, k)
	for i in range(100):
		l = f.next()
	print sum([int(i) for i in str(l[0])])

def edenom(iterations):
	special = 2*iterations/3
	count = iterations
	while count >= 0:
		if count%3 == 2:
			yield special
			special-=2
		else:
			yield 1
		count+=1


def fractiter(initial, denom):
	on = 0
	od = 1

	while True:
		yield (od*initial+on, od)
		const = denom.next()
		nn = od
		nd = on + const * od

		on = nn
		od = nd

if __name__ == "__main__":
	euler65()
