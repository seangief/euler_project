from itertools import combinations
from collections import defaultdict

def euler90():
	dice = set(combinations([0,1,2,3,4,5,6,6,7,8], 6))
	reqs = {
			0: frozenset([1,4,6]),
			1: frozenset([6,0,8]),
			2: frozenset([5]),
			3: frozenset([6]),
			4: frozenset([0,6]),
			5: frozenset([2]),
			6: frozenset([3,0,1,4]),
			8: frozenset([1])
			}

	compatible = checkdice(dice, reqs)

	ans = 0
	for die, dielist in compatible.iteritems():
		dieval = getval(die)
		lval = sum([getval(x) for x in dielist])
		ans += dieval*lval

	print ans

def checkdice(dice, reqs):
	ansset = defaultdict(list)
	while dice:
		d = dice.pop()
		dset = set(d)
		for die in dice:
			oset = set(die)
			if compare(dset, oset, reqs):
				ansset[d].append(die)
	return ansset

def getval(die):
	g = len([x for x in die if x == 6])
	if g == 1:
		return 2
	else:
		return 1

def compare(dset, oset, reqs):
	compatible = False
	for num in reqs.keys():
		if num in dset and num in oset:
			compatible = reqs[num] <= (dset | oset)
		elif num in dset:
			compatible = reqs[num] <= oset
		elif num in oset:
			compatible = reqs[num] <= dset
		else:
			compatible = False
		if not compatible:
			return compatible
	return compatible

if __name__ == "__main__":
	euler90()

