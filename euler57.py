import fractions
n, d = 3, 2
pairs = []
ans = []
for i in range (1,1001):
	pairs.append((n, d))
	tn, td = n+2*d, n+d
	n, d = tn/fractions.gcd(tn,td), td/fractions.gcd(tn,td)
for pair in pairs:
	if len(str(pair[0])) > len(str(pair[1])):
		ans.append((pair[0],pair[1]))
print len(ans)
