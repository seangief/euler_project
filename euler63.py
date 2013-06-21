#print [a**i for a in range(1,10) for i in range(1,23)]

ans = []
for i in range(1,23):
	for a in range(1,10):
		if len(str(a**i)) == i:
			ans.append(a**i)
print len(ans)
