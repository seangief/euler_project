# This preserves the numerator!!!
def fractiter(initial, denom):
	k = denom()
	od = 1
	on = initial

	while True:
		yield (on, od)
		const = k.next()
		nd = on
		nn = od + const * nd
		od = nd
		on = nn


# This preserves the denominator!!!
def fractiter(initial, denom):
	k = denom()
	od = 1
	on = k.next()

	while True:
		yield (on, od)
		const = k.next()
		nd = on
		nn = od + const * nd
		od = nd
		on = nn
'''
