period = dict()
for i in [j for j in range(2,1000) if j%5 != 0 and j%2 != 0]:
	print i
	decimal = []
	remainders = []
	a,b = divmod(10, i)
	while b not in remainders and b != 0:
		decimal.append(a)
		remainders.append(b)
		a,b = divmod(10*b, i)
	period[i] = len(decimal[decimal.index(a):])
for k in period:
	if period[k] == max(period.values()):
		print k
		print period[k]
