# This code produces 3-tuples of possible digit lenghts for the three numbers involved in the answer.
# k = [(a,b,c) for a in range(1,10) for b in range(1,10) for c in range(1,10) if (c == 9-(a+b) and a+b-2 < c and a+b > c-1)]
# (2,3,4) and (1,4,4)

import itertools

def euler32():
	ansset = []
	digitset = set('123456789')
	perms1 = itertools.permutations(digitset, 3)
	for digits1 in perms1:
		digit1set = set(digits1)
		perms2 = itertools.permutations(digitset-digit1set, 2)
		for digits2 in perms2:
			num1, num2, remainingdigits = int("".join(digits1)), int("".join(digits2)), (digitset-digit1set)-set(digits2)
			num3 = num1*num2
			testdigits = set(str(num3))
			if testdigits >= remainingdigits and len(str(num3)) == len(testdigits) and len(str(num3)) == 4:
				ansset.append((num1, num2, num3))


	perms3 = itertools.permutations(digitset, 4)

	for digits1 in perms3:
		digit1set = set(digits1)
		perms2 = digitset-digit1set
		for digits2 in perms2:
			num1, num2, remainingdigits = int("".join(digits1)), int("".join(digits2)), (digitset-digit1set)-set(digits2)
			num3 = num1*num2
			testdigits = set(str(num3))
			if testdigits >= remainingdigits and len(str(num3)) == len(testdigits) and len(str(num3)) == 4:
				ansset.append((num1, num2, num3))

	print ansset

if __name__ == "__main__":
	euler32()
