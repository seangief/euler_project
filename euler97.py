i, c, u = 1, 0, ""
while c < 7830457:
	c+=1
	i*=2
	u = str(i)
	if len(u) > 10:
		i = int(u[len(u)-10:])
i = i*28433+1
print str(i)[len(str(i))-10:]
#print c, i, 2**c


