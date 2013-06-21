factorials = [reduce(lambda x, y: (x*y), range(1,i+1)) for i in range(1, 102)]
answer = 0
factorials.insert(0,0)

for i in range(1,101):
	for j in range(1,i):
		if factorials[i]/(factorials[j] * factorials[i-j]) > 1000000:
			answer+=1
print answer


