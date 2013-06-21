# so, i has to be <= 10/6 * 10**n
i=1
tens = 1
mutable = False
while mutable == False:
	if float(10)/6*10**tens < i:
		tens+=1
		i = 10**tens
	else:
		i+=1
	s = sorted(str(i))
	if s != sorted(str(2*i)):
		continue
	elif s != sorted(str(3*i)):
		continue
	elif s != sorted(str(4*i)):
		continue
	elif s != sorted(str(5*i)):
		continue
	elif s != sorted(str(6*i)):
		continue
	else:
		mutable = True
print i
