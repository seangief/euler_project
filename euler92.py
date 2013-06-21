counter = 0
for i in range(10000000):
	while repeating == False:
		squares = []
		val = 0
			for digit in str(i):
				val += digit**2
	if val == 89:
		counter += 1
		repeating = True
	elif val in squares:
		repeating = True
	
