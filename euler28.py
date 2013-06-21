answer = [1]
counter = 1
twopower = 1
while (counter <= 1001**2):
	for i in range(4):
		counter+=2*twopower
		if counter > 1001**2:
			break
		else:
			answer.append(counter)
	twopower +=1
#print answer
print sum(answer)
