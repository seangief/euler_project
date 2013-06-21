ans = []
for i in range(2,1000000):
	val=0
	for digit in str(i):
		val+=int(digit)**5
	if val == i:
		ans.append(i)
print sum(ans)
